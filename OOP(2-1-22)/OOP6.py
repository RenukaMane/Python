class Demo:
    A = 10;

    def __init__(self):
        print("Inside constructor");
        self.B = 20;

    def __del__(self):
        print("Inside destructor");

    def fun_instance(self):  #Instance method
        print("Inside Instance Method");
        print(self.A);
        print(self.B);
        print(Demo.A);

    @classmethod
    def fun_class(cls):  #class method
        print("Inside class method")
        print(cls.A);       #cls.A is same as Demo.A
        print(Demo.A);
        print(cls.B);


    @staticmethod
    def fun_static():
        print("Inside static method");
        print(Demo.A);
        #print(Demo.B);


def main():
    #obj = Demo();
    #obj.fun_instance();
    #Demo.fun_class();
    Demo.fun_static();


if __name__ == "__main__":
    main();
  