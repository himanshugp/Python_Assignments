
def main():
    num = int(input("Enter a mumber : "))

    for i in range(1, num+1):
        for x in range(1, i+1):
            print(x, end="")
        print()

if __name__ == "__main__":
    main()