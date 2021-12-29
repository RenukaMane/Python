def Area(radius,PI = 3.14):
    ans = 0.0;
    ans = PI * radius * radius;
    return ans;


def main():
    print("Enter the value of radius");
    val = float(input());
    ret = Area(val,7.10);
    #ret = Area(PI = 7.10,radius = val)
    print("Area: ",ret);



if __name__ == "__main__":
    main();