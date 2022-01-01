#Encapsulation -> Characteristic + Behaviours

#Class Definition
class Arithmetic:
    def __init__(self,a,b):  #Constructor
        print("Inside the constructor");
        self.no1 = a #Characteristic
        self.no2 = b  #Characteristic

    def Addition(self): #Behaviour
        ans = self.no1 + self.no2
        return ans

def main():   #POP Code
    print("Enter first number :");
    X = int(input());
    
    print("Enter second number :");
    Y = int(input());

    obj = Arithmetic(X,Y);
    ret = obj.Addition()

    print("Addition: ",ret);

if __name__ == "__main__":
    main()
