import sys

def Display():
    for i in range(4):
        print("Marvellous")

def DisplayX():
    print("Using while loop");
    i = 0;
    while(i<4):
        print("Marvellous")
        i = i+1

def DisplayR(no):
    print("no = ",no);
    no = no + 1;
    DisplayR(no);

def main():
    no= sys.getrecursionlimit();
    print(no);
    #Display();

    #DisplayX();
    #DisplayR(1);

if __name__ == "__main__":
    main();