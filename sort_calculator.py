def main():
    try:
        a=input().split()
        number=[]
        cnt=0

        for i in a:
            num=float(i)
            cnt+=1
            number.append(num)

        for j in range(cnt):
            for k in range(0,cnt-j-1):
                if number[k]>number[k+1]:
                    tmp=number[k]
                    number[k]=number[k+1]
                    number[k+1]=tmp
    
    except ValueError:
        print("Invalid input.")
        return
    
    print(number)

if __name__=="__main__":
    main()

            
        
        

    
