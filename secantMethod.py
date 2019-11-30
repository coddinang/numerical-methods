
import math

def function(x):
    f = 3*x +math.sin(x) -math.exp(x)
    return f

def runMethod(x_i_1, x_i, i):

    iterator = 0
    while True:
        f_i_1 = function(x_i_1)
        f_i = function(x_i)
        subs = x_i-x_i_1
        x_next = x_i -(f_i*subs/(f_i-f_i_1))

        print("x_{} = {}".format(iterator, round(x_next, 4)))

        if iterator == i:
            break
        x_i_1 = x_i
        x_i = x_next
        iterator = iterator +1

# run
runMethod(0, 1, 6)
