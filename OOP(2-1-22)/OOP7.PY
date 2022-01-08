class Demo:
    def __init__(self):
        self.A = 10;
        self.__B = 20; #private variable of class i.e abstraction

    def Display(self):
        print("Inside Fun")
        print(self.A);
        print(self.__B);

def main():
    obj = Demo();
    print(obj.A);
    #print(obj.__B);
    obj.Display();

if __name__ == "__main__":
    main();

    #A is a public variable
    #B is a private variable