def Addition(no1,no2):
    Ans = 0
    Ans = no1 + no2;
    return Ans;


def main():
    print("Enter 1st no");
    val1 = int(input());

    print("Enter 2nd no");
    val2 = int(input());

    ret = Addition(val1,val2);
    print("Addition is: ",ret);




if __name__ == "__main__":
    main();