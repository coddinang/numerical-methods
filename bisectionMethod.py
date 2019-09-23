import math


def bisectionMethod(a_n, b_n):
    i = 1
    c_before = 0
    while True:

        f_a = function(a_n)
        c_n = (a_n + b_n) / 2
        f_c = function(c_n)

        sig = f_a * f_c

        print("the iterator", i, "and value", c_n)
        if i > 1:
            ERROR = math.fabs((c_n - c_before) / c_n)
            if ERROR == 0:
                print("the answer:", c_n)
                break

        if sig > 0:
            a_n = c_n
        elif sig < 0:
            b_n = c_n
        c_before = c_n
        i=i+1


def function(x):
    f = math.pow(x, 3) - x - 2
    return f


# RUN
bisectionMethod(1, 2)
