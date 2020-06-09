import math
print("QUADRATIC EQUATION CALCULATOR")
print("input the value of a,b,c")
while True:
    try:
        a=float( input("input a"))
        b=float(input( "input b"))
        c=float(input("input c"))
        m= 4*a*c
        y=b*b
        n=y-m
        h=2*a
        d=str(h)
        q=str(-b)
        if n<0:
            try:
                i=-1
                z=(i*n)
                p=math.sqrt(z)
                v=str(p)
                print('first root is '+"(" +q + '+' +v+'i'+')'+'/'+d)
                print('second root is '+"(" +q + '-' +v+'i'+')'+'/'+d)
            except:
                print("Synthax Error!!")
        elif n>0:
            try:
                f= math.sqrt(n)
                j=(-b+f)/(2*a)
                k=(-b-f)/(2*a)
                s= str(j)
                t=str(k)
                print('first root is= ' +s)
                print('second root is= ' +t)
            except:
                print ("MATH ERROR!!")
    except:
        print("input not supported, Retry>>")                
    
