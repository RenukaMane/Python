def Addition(val1,val2):
    ans = 0;
    ans = val1 + val2;
    return ans;

###################################
def main():
    no1 = 0;
    no2 = 0;
    
    
    print("Enter first number");
    no1 = int(input());

    print("Enter second number");
    no2 = int(input());

    ret = Addition(no1,no2);
    print("Addition is:",ret);

###################################

if __name__ == "__main__":
    main();

####################################    