import math
while True:
    R = 70
    L = 150
    Q = int(input("input the value of thetha"))
    a = (R*R)/(L*L)
    b = math.sin(math.radians(Q))
    c = b*b
    d = 1 - (a*c)
    e = math.sqrt(d)
    x = R + L -( R* math.cos(math.radians(Q)) + L *e)
    X = str(x)
    print ( "the theoretical position is >>"+ X)
    
