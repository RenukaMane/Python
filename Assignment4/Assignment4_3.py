#from functools import reduce;
import functools;

checkRange = lambda a :(a>=70 and a<=90)

Increment = lambda a : (a+10)

mul = lambda a,b : (a*b);

def main():
    #data = [10,21,3,1,74,85,90,88];
    data = [];
    print("Enter no. of elements in list")
    tot = int(input());

    print("Enter the elements");
    for i in range(tot):
        val = int(input());
        data.append(val);

    print(data);

    #filtering the data
    data1 = list(filter(checkRange,data))
    print(data1);

    #mapping the data
    data2 = list(map(Increment,data1));
    print(data2);

    #reduce to find multiplication
    res = functools.reduce(mul,data2);
    print("Result: ", res);

if __name__ == "__main__":
    main()