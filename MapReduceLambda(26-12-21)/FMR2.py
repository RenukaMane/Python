from functools import reduce;

def main():
    data = [5,6,7,8,4];
    
    #filter(funct,list)
    newData = list(filter(lambda no : (no%2==0),data));
    print(newData);
   
    #map(funct,list)
    newData1 = list(map(lambda no : (no+2),newData));
    print(newData1);

    ret = reduce(lambda a,b : (a+b),newData1);
    print(ret);
    

if __name__ == "__main__":
    main();