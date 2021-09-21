# we need the math library
import math


def bisectionMethod(a_n, b_n, func):
    i = 1
    c_before = 0
    while True:

        f_a = func(a_n)
        c_n = (a_n + b_n) / 2
        f_c = func(c_n)

        sig = f_a * f_c

        print(f'the iterator {i} and value {c_n}')
        if i > 1:
            # calculate the ERROR when 'i' is greater than 1 (i>1)
            error = math.fabs((c_n - c_before) / c_n)
            if error == 0:
                print(f'the answer: {c_n}')
                break

        if sig > 0:
            a_n = c_n
        elif sig < 0:
            b_n = c_n
        c_before = c_n
        i += 1

if __name__ == '__main__':
    a_value = 1
    b_value = 2
    
    def math_function(x):
        """
        This is a math function
        """
        return x**3 - x - 2 
    
    bisectionMethod(a_value, b_value, math_function)