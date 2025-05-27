
def main():
    num = int(input("Number of elements : "))
    noList = []

    for i in range(num):
        noList.append(int(input("Enter number for list.")))

    if not noList:
        print("List is empty.")

    else:
        minimum = noList[0]

        for n in noList:
            if n < minimum:
                minimum = n

        print("Minimum number is : ", minimum)

if __name__ == "__main__":
    main()