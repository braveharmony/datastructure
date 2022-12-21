from mydeque import*

x=mydeque()
x.add_rest(1)
x.add_first(2)
x.add_rest(4)
x.remove_rest()
x.add_rest(5)
x.add_rest(8)
print("x is",x)
print("structure of x is",str(x).split())
print("length of x is",len(x))
print("x[-4] is",x[-4],"and x[2] is",x[2])
print("max value of x is",max(x),"and min value of x is",min(x))
for i in x:
    print(i)