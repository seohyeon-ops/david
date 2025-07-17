def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0 :
        return "Error: Division by zero."
    return a/b

def main():
    a=input("Enter first expression:").split()

    L=[]
    for i in a:
        L.append(i)
    
    try:
        a=float(L[0])
    except ValueError:
        print("Invalid number input.")
        return
    try:
        b=float(L[2])
    except ValueError:
        print("Invalid number input.")
        return

    t=(L[1])

    if t=="+":
        result=add(a,b)
    elif t=="-":
        result=subtract(a,b)
    elif t=="*":
        result=multiply(a,b)
    elif t=="/":
        result=divide(a,b)
    else:
        result="Invalid operator."

    print("Result:", result)

if __name__ == "__main__":
    main()
