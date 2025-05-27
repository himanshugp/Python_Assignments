
def main():
    n1 = int(input("Enter first number : "))

    n2 = int(input("Enter second number : "))

    Multiplicaion = lambda No1, No2 : No1 * No2

    ret = Multiplicaion(n1, n2)
    print("Power of Two is : ",ret)

if __name__ == "__main__":
    main()