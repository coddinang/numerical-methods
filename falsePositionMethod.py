
import math

def function(x):
    f = math.exp(-x)*(3.2*math.sin(x)-0.5*math.cos(x))
    return f

def runMethod(x_a, x_b):
    i = 0
    c_before = 0
    print("| a | b | f(a) | f(b) | c | f(c) |")
    
    while True:
        f_a = function(x_a)
        f_b = function(x_b)
        subs = x_b -x_a
        c = x_a -(subs*f_a/(f_b-f_a))
        f_c = function(c)
        print("| {} | {} | {} | {} | {} | {} |".format(
            round(x_a,4), round(x_b,4), round(f_a,4),
            round(f_b,4), round(c,4), round(f_c,4)))

        if i >0:
            ERROR = math.fabs((c-c_before)/c)
            if ERROR ==0:
                break

        sig = f_a*f_c
        if sig >0:
            x_a = c
        elif sig < 0:
            x_b =c
        c_before = c
        i =i+1

# run
runMethod(1,2)
    
