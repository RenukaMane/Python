def Addition(*val):
    sum = 0;
    for i in val:
        sum = sum + i;
    return sum;



def main():
    ret = Addition(10,20,30,40);
    print("Addition is: ",ret);

if __name__ == "__main__":
    main();