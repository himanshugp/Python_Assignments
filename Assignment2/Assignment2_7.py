
def main():
    num = int(input("Enter number : "))

    for i in range(num):
        for x in range(1, num+1):
            print(x, end='')
        print()

if __name__ == "__main__":
    main()