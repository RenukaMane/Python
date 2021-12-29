from functools import reduce;

#def checkEven(no):
#    return (no%2 == 0)

checkEven = lambda no : (no%2==0)

#def Increment(no):
#    return no+2;

Increment = lambda no : (no + 2);

#def Addition(a,b):
#    return a+b;

Addition = lambda a,b : (a+b);

def main():
    data = [5,6,7,8,4];
    
    #filter(funct,list)
    newData = list(filter(checkEven,data));
    print(newData);
   
    #map(funct,list)
    newData1 = list(map(Increment,newData));
    print(newData1);

    ret = reduce(Addition,newData1);
    print(ret);
    

if __name__ == "__main__":
    main();