
def main():
    print("Number of stars you want : ")
    number = int(input())

    # from google search
    print(" * " * number)

    # self logic
    for i in range(number): 
        print("*") 

if __name__ == "__main__":
    main()