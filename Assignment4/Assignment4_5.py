from functools import reduce

def main():
    Data = []

    print("Enter number of elements : ")
    Size = int(input())

    print("Please enter numeric values : ")
    for i in range(Size):
        no = int(input())
        Data.append(no) 

    FData = list(filter(lambda No: No > 1 and all(No % i != 0 for i in range(2, No)), Data))
    print("Filter output : ",FData)

    MData = list(map(lambda No : No * 2, FData))
    print("Map output : ",MData)

    RData = reduce(lambda No1, No2: No1 if No1 > No2 else No2, MData)
    print("Reduce output : ",RData)

if __name__ == "__main__":
    main()