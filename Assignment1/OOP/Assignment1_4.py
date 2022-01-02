class Demo:
    def __init__(self,val):
        self.no = val;

    def Display(self):
        for i in range(self.no):
            print("Marvellous Systems");


def main():
    print("Enter the no");
    no = int(input());

    obj1 = Demo(no);
    obj1.Display();

if __name__ == "__main__":
    main();
    

