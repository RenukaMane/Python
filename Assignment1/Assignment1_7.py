#Write a program which contains one function that accept one number from user and returns 
#true if number is divisible by 5 otherwise return false. 

def Division():
    print("Enter number");
    no = int(input());

    if(no % 5 == 0):
        return True;
    else:
        return False;

def main():
    ans = Division();
    print(ans);

if __name__ == "__main__":
    main();