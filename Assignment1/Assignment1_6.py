#Write a program which accept number from user and check whether that number is positive or 
#negative or zero.

def Funct():
    print("Enter number");
    no = int(input());

    if(no==0):
        print("Number is zero");
    elif(no>0):
        print("Number is positive");
    else:
        print("Number is negative");

def main():
    Funct();

if __name__ == "__main__":
    main();