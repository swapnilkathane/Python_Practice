while(True):
    print('begin')
    x=float (input('Enter the number-'))
    #x=int(n)
    if(x>100):
        print('enter valid marks')
    elif(x>=75 and x<=100):
        print('distinction')
        #print('number is',x)
    elif(x>=60 and x<75):
        print('first class')
    elif(x>=35 and x<60):
        print('pass')
    elif(x>=0 and x<35):
        print('fail')
    else:
        print('not valid marks')
