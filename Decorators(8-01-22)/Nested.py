def outer():
    print("Inside Outer function");

    def Inner():
        print("Inside Inner function")

    return Inner  #actual funtion cha object return hoto
    #return Inner();

def main():
    #outer();
    func_Inner = outer();
    func_Inner();



if __name__ == "__main__":
    main();