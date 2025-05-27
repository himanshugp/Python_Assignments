
def main():
    num = int(input("Number of elements : "))
    noList = []

    for i in range(num):
        noList.append(int(input("Enter number for list.")))

    if not noList:
        print("List is empty.")

    else:
        searchNum = int(input("Element to search : "))
        frequency = 0

        for n in noList:
            if n == searchNum:
                frequency = frequency + 1

        print("Frequency of no : ",frequency)

if __name__ == "__main__":
    main()