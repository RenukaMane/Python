import Marvellous

def main():
    size = 0;
    i=0;
    data = [];

    print("How many elements you want?");
    size = int(input());
   
    print("Enter the elements");

    for i in range(size):
        data.append(int(input()));

    print("Your entred data is: ",data);\

    ret = Marvellous.Addition(data);

    print("Addition is: ",ret);


if __name__ == "__main__":
    main();