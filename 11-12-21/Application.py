#import Marvellous
#from Marvellous import *
import Marvellous as M
import Infosystem

def main():
    print("Inside module:",__name__)
    no1 = int(input("Enter first number :"))
    no2 = int(input("Enter second number"))

    ret = M.Addition(no1,no2)
    ret1 = Infosystem.Subtraction(no1,no2)
    print("Addition is :",ret);
    print("Subtraction is :",ret1);

if __name__ == "__main__":
    main()