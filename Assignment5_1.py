Sum = lambda n1, n2 : n1 + n2
Dif = lambda n1, n2 : n1 - n2
Prod = lambda n1, n2 : n1 * n2
Div = lambda n1, n2 : n1 / n2

def main():
    No1 = int(input("Enter first number : "))

    No2 = int(input("Enter second number : "))

    print("Sum : ", Sum(No1, No2))
    print("Difference : ", Dif(No1, No2))
    print("Multiplication : ", Prod(No1, No2))
    print("Division : ", Div(No1, No2))

if __name__ == "__main__":
    main()