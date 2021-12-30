from functools import reduce;


checkEven = lambda a : (a%2 == 0)

square = lambda a : (a**2)

Add = lambda a,b : (a+b);

def main():
    data = [];
    print("Enter the no of elements in list");
    tot = int(input());
    print("Enter the elements");
    for i in range(tot):
        val = int(input());
        data.append(val);
    print(data);

    #filter for even nos
    data1 = list(filter(checkEven,data));
    print("Even: ",data1);

    #map fun to find the squares
    data2 = list(map(square,data1));
    print("Square: ",data2);

    #reduce function
    res = reduce(Add,data2);
    print("Addition: ",res);


if __name__=="__main__":
    main();