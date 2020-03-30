n=int(input('enter the number'))
#m=int(input('Enter the number of term'))
prev=0
cur=1
print(prev)
print(cur)
p=range(n)
for m in p:
    nxt=prev+cur
    prev=cur
    cur=nxt
    print(nxt)
    if(m==(n-3)):
        break



