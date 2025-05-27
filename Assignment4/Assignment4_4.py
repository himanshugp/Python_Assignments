from functools import reduce

def main():
    Data = []

    print("Enter number of elements : ")
    Size = int(input())

    print("Please enter numeric values : ")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    FData = list(filter(lambda No : (No % 2 == 0), Data))
    print("Filter output : ",FData)

    MData = list(map(lambda No : No*No, FData))
    print("Map output : ",MData)

    RData = reduce(lambda A,B : A+B, MData)
    print("Reduce output : ",RData)

if __name__ == "__main__":
    main()