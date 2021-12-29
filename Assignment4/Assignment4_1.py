
#def square(val):
#    return val ** 2;

square = lambda val : val ** 2;

def main():
    print("Enter a number");
    no = int(input());
    ret = square(no);
    print("Squre = ",ret);

if __name__ == "__main__":
    print("Hello World")
    main(); 
