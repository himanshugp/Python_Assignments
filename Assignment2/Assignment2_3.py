
def main():
    num = int(input("Enter the number : "))

    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    print("Factorial of number : ", factorial)

if __name__ == "__main__":
    main()