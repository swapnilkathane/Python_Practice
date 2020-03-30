#num=int(input('Enter number'))
def factorial(num):
    m=1
    fact=1
    num1=num
    while(m<num):
        fact=num1*m
        num1=fact
        m+=1
    return num1

n1=int(input('Enter value of n '))
n2=int(input('enter value of r '))
n3=(factorial(n1))
n4=(factorial(n2))
n5=(n1-n2)
n6=(factorial(n5))
res=n3/(n4*n6)
print(res)


