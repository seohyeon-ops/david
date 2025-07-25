def main():
    try:
        a=input().split()
        num=[]

        if len(a)==0:
            print("Invalid input.")
            return
        
        for i in a:
            num.append(float(i))
        
        n = len(num)
        
        for i in range(n-1):
            for j in range(n-1-i):
                if num[j]>num[j+1]:
                    num[j],num[j+1] = num[j+1],num[j]
        
        print("Sorted:",end=' ')
        for i in num:
            print("%f" %i,end =' ')
            
        
    except ValueError:
        print("Invalid input.")


if __name__=="__main__":
    main()