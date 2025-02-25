import array
sum=0
a=[1,2,3,4]
x=array.array('i',[])
x.fromlist(a)
for i in x:
    sum+=i
print(sum)
