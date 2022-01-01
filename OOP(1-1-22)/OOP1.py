class Demo:
    A = 10;
    B = 20;
    def __init__(self):
        self.C = 30
        self.D = 40

def main():
    print("Value of A: "Demo.A);
    print("Value of B:",Demo.B);

    obj1 = Demo();
    obj2 = Demo();

    print("Value of C: ",obj1.C);
    print("Value of D:",obj2.C);


    


