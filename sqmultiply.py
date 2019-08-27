import math as m

def exp_func(x, y, n):
    exp = bin(y)
    value = x
 
    for i in range(3, len(exp)):
        value = value * value
        value = value % n
        if(exp[i:i+1]=='1'):
            value = value*x
            value = value % n
        
    return value




#ex = exp_func(3, 4, 100)
#print(ex)
