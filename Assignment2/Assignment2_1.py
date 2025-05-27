import Arithmetic

def main():
    FirstNumber = int(input("Enter first number : "))
    SecondNumber = int(input("Enter second number : "))

    ret = Arithmetic.Add(FirstNumber, SecondNumber)
    print("Addition is : ",ret)
    ret = Arithmetic.Sub(FirstNumber, SecondNumber)
    print("Substraction is : ",ret)
    ret = Arithmetic.Mult(FirstNumber, SecondNumber)
    print("Multiplication is : ",ret)
    ret = Arithmetic.Div(FirstNumber, SecondNumber)
    print("Division is : ",ret)

if __name__ == "__main__":
    main()