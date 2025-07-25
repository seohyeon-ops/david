def main():
    try:
        a=input().split()
        number=[]

        for i in a:
            num=float(i)
            number.append(num)
    
        mn=number[0]
        mx=number[0]

        for j in number:
            if j<mn:
                mn=j
            if j>mx:
                mx=j
        
        print("Min: %.1f,Max: %.1f" %(mn,mx))
    
    except ValueError:
        print("Invalid input.")
        return

if __name__=="__main__":
    main()
