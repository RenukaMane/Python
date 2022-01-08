def Division(A,B):
    Ans = 0.0;
    Ans = A/B
    return Ans;
    
def SmartDivision(Func_Name):
    def Inner(a,b):
        if a < b:
            a,b = b,a;
        return Func_Name(a,b);


Division = SmartDivision(Division)

def main():
    No1 = int(input("Enter first no"));
    No2 = int(input("Enter second no"));

    ret = Division(No1,No2);

    print("Div = ",ret)

if __name__ == "__main__":
    main();