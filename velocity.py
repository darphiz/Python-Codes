import math
calculating = True
while calculating:
    R = 70
    L = 150
    W = 20.94
    Q = int(input("input the value of thetha"))
    a = R* math.sin(math.radians(2 * Q)) #Rsin2Thetha
    b =  math.sin(math.radians(Q)) #sin thetha
    c = b*b #sin square thetha
    d = (L*L) - (R*R*c) #Lsquare -rsquare
    e = math.sqrt(d) # raise to pwerhalf
    f = 2*e
    g = a/f
    h= math.sqrt(-1*(b + g))
    x= R*W*h
    X = str(x)
    print ( "the velocity is >>"+ X)
    
