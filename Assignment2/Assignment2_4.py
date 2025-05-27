def AdditionOfFactors(n):
    total = 0
    for i in range(1, n): # if up to the number as well n+1
        if n % i == 0:
            total += i

    return total

def main():
    num = int(input("Enter the number : "))

    addition = AdditionOfFactors(num)

    print("Factorial of number : ", addition)

if __name__ == "__main__":
    main()