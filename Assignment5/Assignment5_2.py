class Circle:
    PI = 3.14;
    def __init__(self):
        self.radius = 0.0;
        self.area = 0.0;
        self.circumference = 0.0;

    def Accept(self):
        print("Enter radius of the circle");
        self.radius = int(input());

    
    def CalculateArea(self):
     
        self.area = Circle.PI * self.radius * self.radius;

    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI *self.radius;

    def Display(self):
        print("Radius: ",self.radius);
        print("Area : ",self.area);
        print("Circumference: ",self.circumference);


def main():
    #First object
    obj1 = Circle();
    obj1.Accept();
    obj1.CalculateArea();
    obj1.CalculateCircumference();
    obj1.Display();

    #Second Object
    obj2 = Circle();
    obj2.Accept();
    obj2.CalculateArea();
    obj2.CalculateCircumference();
    obj2.Display();



if __name__ == "__main__":
    main();