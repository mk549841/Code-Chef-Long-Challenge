for _ in range(int(input())):
    n=int(input())
    print("O",end="")
    k=n-1
    i=0
    r=7
    while(i<k):
       
        print(".",end="")
       
        i+=1
        r-=1
        if(r==0):
            print()
            r=8
    k=64-n
    i=0
    while(i<k):
        print("X",end="")
       
        i+=1
        r-=1
        if(r==0):
            print()
            r=8
    print()
