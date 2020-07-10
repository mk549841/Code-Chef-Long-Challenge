for _ in range(int(input())):
    n=int(input())
    h=0
    o=0
    for j in range(n):
        p,w=map(str,input().split())
        t=0
        t1=0
        for i in p:
            t+=int(i)
        for i in w:
            t1+=int(i)
        if t==t1:
            h+=1
            o+=1
        elif t>t1:
            h+=1
        elif t1>t:
            o+=1
    if h>o:
        print(0,h)
    elif o>h:
        print(1,o)
    else:
        print(2,h)
