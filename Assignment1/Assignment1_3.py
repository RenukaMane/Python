#Write a program which contains one function named as Add() which accepts two numbers 
#from user and return addition of that two numbers.

def Add():
    print("Enter 1st number");
    no1 = int(input());

    print("Enter 2nd number");
    no2 = int(input());

    ans = no1 + no2;

    return ans

def main():
    ret = Add();
    print("Addition = ",ret);

if __name__ == "__main__":
    main();