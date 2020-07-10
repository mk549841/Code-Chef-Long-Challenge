from functools import reduce
for _ in range(int(input())):
    n=int(input())
    li=[]
    li1=[]
    for i in range(4*n-1):
        m,n=map(int,input().split())
        li.append(m)
        li1.append(n)
    r =reduce(lambda x, y: x ^ y,li)
    print(r,end=' ')
    r =reduce(lambda x, y: x ^ y,li1)
    print(r,end=' ')
    print()
