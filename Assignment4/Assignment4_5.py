from functools import reduce;

def prime(no):
    flag = 0;
    val = int(no/2);
    for i in range(2,val):
        if(no%i==0):
            flag = 1;
            break;
    if(flag==0):
        return True;
    else:
        return False;


mul = lambda a: a*2;

def max(a,b):
    if(a>b):
        return a;
    else:
        return b;


def main():
    data = [];
    print("Enter the no of elements in list");
    tot = int(input());
    print("Enter the elements");
    for i in range(tot):
        val = int(input());
        data.append(val);
    print(data);

    #filter funtion to find prime nos
    data1 = list(filter(prime,data));
    print("Prime: ",data1);

    #map function to multiply no by 2
    data2 = list(map(mul,data1));
    print("MMultiplication: ",data2);

    #reduce function to return max no
    res = reduce(max,data2);
    print("Max: ",res);

if __name__ == "__main__":
    main();