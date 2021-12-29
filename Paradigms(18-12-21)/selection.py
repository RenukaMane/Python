def max(val1,val2):

    if(val1>val2):
        return val1;
    else:
        return val2;      

def main():

    print("Enter no1");
    no1 = int(input());

    print("Enter no2");
    no2 = int(input());

    ret = max(no1,no2);
    print("Max no = ",ret);    



if __name__ == "__main__":
    main();