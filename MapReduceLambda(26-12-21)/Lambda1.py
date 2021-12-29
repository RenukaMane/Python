def Add(val1,val2):
    return val1 + val2;

AddX = lambda a,b : a+b;

def main():
    ret = Add(10,20);
    print("Addition is: ",ret);
    print(type(Add));
    
    fn = AddX(10,20);
    print("Lambda Addition: ",fn);
    print(lambda a,b : a+b);

if __name__ == "__main__":
    main();