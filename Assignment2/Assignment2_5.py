def CheckIfPrime(No):
    for i in range(2, No):
        if (No % i) == 0:
            return True
        else:
            return False
        
def main():
    num = int(input("Enter a number : "))

    IsPrime = CheckIfPrime(num)
    if IsPrime == True:
        print("Not Prime No.")
    else:
        print("Prime Number.")

if __name__ == "__main__":
    main()