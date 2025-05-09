
def main():
    print("Enter number :")
    number = int(input())

    if number == 0:
        print("Zero")
    elif number < 0:
        print("Negative Number")
    else:
        print("Positive Number")

if __name__ == "__main__":
    main()