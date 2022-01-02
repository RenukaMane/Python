class EvenOdd:
    def __init__(self,num):
        self.no = num;

    def chkNum(self):
        if(self.no%2==0):
            print("Even number");
        else:
            print("Odd number");




def main():
    print("Enter a number");
    no = int(input());

    obj1 = EvenOdd(no);
    obj1.chkNum();


if __name__ == "__main__":
    main();