
def Add(val1,val2):
    return val1 + val2;



def main():
    print("Enter no1");
    no1 = int(input());

    print("Enter no2");
    no2 = int(input());

    ans = Add(no1,no2);
    print("Addition = ",ans);

if __name__ == "__main__":
    main();