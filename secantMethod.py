import math

def secant_method(x_i_1, x_i, i, func):
    iterator = 0
    while True:
        f_i_1 = func(x_i_1)
        f_i = func(x_i)
        subs = x_i-x_i_1
        x_next = x_i - (f_i*subs/(f_i-f_i_1))

        print("x_{} = {}".format(iterator, round(x_next, 4)))

        if iterator == i:
            break
        x_i_1 = x_i
        x_i = x_next
        iterator += 1


if __name__ == '__main__':

    def math_function(x):
        """
        This is a math function: f(x) = 3*x + sin(x) - e^x
        """
        return 3*x + math.sin(x) - math.exp(x)

    secant_method(0, 1, 6, math_function)
