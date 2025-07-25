def main():
    try:
        a=float(input("Enter number:"))
    except ValueError:
        print("Invalid number input.")
        return
    
    try:
        b=int(input("Enter exponent:"))
    except ValueError:
        print("Invalid exponent input.")

    result = 1.0

    if b==0:
        result=1.0
    elif b>0:
        result=a
        for _ in range(b-1):
            result*=a
    else:
        result=a
        for _ in range(abs(b)-1):
            result*=a
        result=1/result
    
    print("Result:%.3f" %result)

if __name__=="__main__":
    main()










