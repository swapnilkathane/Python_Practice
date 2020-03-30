print('begin')
x=int (input("Enter positive number"))
a=2
p=0
while(a<x):
    if(x%a!=0):
        b=1 #print('given number is prim number')
    else:
        p+=1
        #print('not prime number')
    a+=1
if(p==0):
    print('prime number')
else:
    print('not prime')
