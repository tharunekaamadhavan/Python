def hack(n):
    a=[]
    for i in n:
        a.append(i)
    a.sort()
    a.reverse()
    b=""
    for j in a:
        b=b+j
    print(b)
n="425434"
hack(n)
