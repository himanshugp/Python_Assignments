
def main():
    num = int(input("Number of elements : "))
    noList = []
    sum = 0

    for i in range(num):
        noList.append(int(input("Enter number for list.")))

    for n in noList:
        sum = sum + n

    print("Sum is :", sum)

if __name__ == "__main__":
    main()