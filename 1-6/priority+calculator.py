def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Error:Division by zero."
    return a/b

def calculate(token):
    if len(token)%2==0:
        return "Invalid input."
    
    try:
        for i in range(0,len(token),2):
            token[i]=float(token[i])
    except ValueError:
        return "Invalid input."
    
    index = 1
    while index < len(token)-1:

        if token[index]=='*':
            result = multiply(token[index-1],token[index+1])
        
        elif token[index]=='/':
            result = divide(token[index-1],token[index+1])
            if result == "Error:Division by zero.":
                return result
        else:
            index+=2
            continue

        token[index-1:index+2]=[result]
        index=1
    
    index=1
    while index < len(token)-1:
        if token[index] == '+':
            result=add(token[index-1],token[index+1])
        elif token[index] == '-':
            result=subtract(token[index-1],token[index+1])
        else:
            return "Invalid input."
        
        token[index-1:index+2]=[result]
        index=1
    

    return f"{token[0]:.1f}"


def main():
    try:
        token=input().split()
        result = calculate(token)
        if result in ["Invalid input.","Error: Division by zero."]:
            print(result)
        else:
            print("Result:",result)
    except ValueError:
        print("Invalid input.")


if __name__=="__main__":
    main()