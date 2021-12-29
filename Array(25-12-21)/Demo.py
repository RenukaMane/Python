import array as arr;

def printArr(a):
    for i in range(len(a)):
        print(a[i])


def main():
    print("Hello world")
    a = arr.array('f',[1.5,2,3,4]);
    printArr(a);

if __name__ == "__main__":
    main();

 