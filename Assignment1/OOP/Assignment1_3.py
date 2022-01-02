class Maths:
    def __init__(self,a,b):
        self.no1 = a;
        self.no2 = b;

    def Add(self):
        return self.no1 + self.no2;

def main():
    print("Enter 1st number");
    no1 = int(input());

    print("Enter 2nd number");
    no2 = int(input());

    obj1 = Maths(no1,no2);
    ans = obj1.Add();
    print("Addition is: ",ans);

if __name__ == "__main__":
    main();
