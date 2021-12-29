mul = lambda a,b : a * b;

def main():
    print("Enter 1st number");
    no1 = int(input());
    print("Enter 2nd number");
    no2 = int(input());

    ret = mul(no1,no2);
    print("Multiplication = ",ret);

if __name__ == "__main__":
    main();