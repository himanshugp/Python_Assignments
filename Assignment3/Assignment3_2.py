
def main():
    num = int(input("Number of elements : "))
    noList = []

    for i in range(num):
        noList.append(int(input("Enter number for list.")))

    if not noList:
        print("List is empty.")

    else:
        maximum = noList[0]

        for n in noList:
            if n > maximum:
                maximum = n

        print("Maximum number is : ", maximum)

if __name__ == "__main__":
    main()