
def ChkNum(Number):
    if Number % 2 == 0:
        print("Even number.")
    else:
        print("Odd number.")

def main():
    print("Enter number : ")
    num = int(input())

    ChkNum(num)

if __name__ == "__main__":
    main()