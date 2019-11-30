
import math

def functionOriginal(x):
    f = math.cos(x) -math.pow(x, 3)
    return f

def functionDerived(x):
    f_d = -math.sin(x) -3*x**2
    return f_d

def runMethod(x_0):
    iterator = 1
    while True:
        f = functionOriginal(x_0)
        f_d = functionDerived(x_0)
        x_next = x_0 -(f/f_d)

        print("x_{} = {}".format(iterator, x_next))
        if iterator == 6:
            break
        x_0 = x_next
        iterator = iterator + 1

# run
runMethod(0.5)
