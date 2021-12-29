#Write a program which contains one function named as ChkNum() which accept one
#parameter as number. If number is even then it should display “Even number” otherwise
#display “Odd number” on console.

def OddEven(val):
    if(val%2 == 0):
        print("Even");
    else:
        print("False");

def main():

    print("Enter a number");
    no = int(input());
    OddEven(no);

    
if __name__ == "__main__":
    main();