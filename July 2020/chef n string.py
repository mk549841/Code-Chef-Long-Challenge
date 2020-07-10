# cook your dish here
for _ in range(int(input())):
    n=int(input())
    t=[]
    li=list(map(int,input().split()))
    for i in range(0,len(li)-1):
        x=li[i+1]-li[i]-1
        if x<0:
            x=li[i]-li[i+1]-1
        t.append(x)
    print(sum(t))
    
            
            
    
    
