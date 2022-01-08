class Demo:
    A = 10;

    def __init__(self):
        print("Inside constructor");
        self.B = 20;

    def __del__(self):
        print("Inside destructor");

    def fun_instance(self):  #Instance method
        print("Inside Instance Method");

    @classmethod
    def fun_class(cls):  #class method
        print("Inside class method")


    @staticmethod
    def fun_static():
        print("Inside static method");



def main():
    Demo.fun_class();
    Demo.fun_static();
    obj = Demo();
    obj.fun_instance();

    obj.fun_static();
    obj.fun_class();

if __name__ == "__main__":
    main();
  