
def Add(Number1, Number2):
    add = Number1 + Number2
    return add

def main():
    print("Enter first number : ")
    num1 = int(input())

    print("Enter second number : ")
    num2 = int(input())

    Addition = Add(num1, num2)
    print("Addition is :", Addition)

if __name__ == "__main__":
    main()