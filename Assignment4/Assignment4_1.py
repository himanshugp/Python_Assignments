
def main():
    n = int(input("Enter the number : "))

    PowerOfTwo = lambda No : No * No

    ret = PowerOfTwo(n)
    print("Power of Two is : ",ret)

if __name__ == "__main__":
    main()