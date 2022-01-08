class Demo:
    def __init__(self):
        self.A = 10;
        self.__B = 20; #private variable of class i.e abstraction

    def fun(self):
        print("Inside fun");
        self.__gun();


    def __gun(self):
        print("Inside gun");
        self.__B = 100;
        print(self.__B);

def main():
    obj = Demo();
    obj.fun();
    #obj.__gun()

if __name__ == "__main__":
    main();

    #A is a public variable
    #B is a private variable