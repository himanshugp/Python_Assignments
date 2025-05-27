import MarvellousNum

primeNos = []

def ListPrime(no):
    global primeNos
    if MarvellousNum.CheckPrime(no):
        primeNos.append(no)

def Sum():
    global primeNos

    sum = 0
    for n in primeNos:
        sum = sum + n
    
    return sum


def main():
    num = int(input("Number of elements : "))
    noList = []

    for i in range(num):
        noList.append(int(input()))

    for x in noList:
        ListPrime(x)

    ret = Sum()
    print("Sum of prime numbers is : ",ret)
        

if __name__ == "__main__":
    main()