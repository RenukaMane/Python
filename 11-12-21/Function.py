def Arithmatic(no1,no2):
    add = no1 + no2
    sub = no1 - no2
    return add,sub

def main():
    print("Enter 1st no : ")
    val1 = int(input())
    

    print("Enter second number : ")
    val2 = int(input())

    ret1,ret2 = Arithmatic(val1,val2)
    print("Addition is : ",ret1)
    print("Subtraction is ",ret2)

if __name__=="__main__":
    main()