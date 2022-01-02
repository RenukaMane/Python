class Arithmetic:
    def __init__(self,a,b):
        self.val1 = a;
        self.val2 = b;
        

    def Addition(self):
        return self.val1 + self.val2;

    def Subtraction(self):
        return self.val1 - self.val2;

    def Multiplication(self):
        return self.val1 * self.val2;

    def Division(self):
        return self.val1 / self.val2;



def main():
    print("Enter no1");
    no1 = int(input());

    print("Enter no2");
    no2 = int(input());

    obj1 = Arithmetic(no1,no2);
    
    add = obj1.Addition();
    print("Addition = ",add);

    sub = obj1.Subtraction();
    print("Subtraction = ",sub);

    mul = obj1.Multiplication();
    print("Multiplication = ",mul);

    div = obj1.Addition();
    print("Division = ",div);



if __name__ == "__main__":
    main()