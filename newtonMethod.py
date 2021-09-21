
import math

def newton_method(x_0, iter_to, func_original, func_derived):
    iterator = 1
    while True:
        f = func_original(x_0)
        f_d = func_derived(x_0)
        x_next = x_0 - (f/f_d)

        print("x_{} = {}".format(iterator, x_next))
        if iterator == iter_to:
            break
        x_0 = x_next
        iterator += 1


if __name__ == '__main__':

    def function_original(x):
        """
        This is the original function: f(x) = cos(x) - x^3
        """
        return math.cos(x) - math.pow(x, 3)


    def function_derived(x):
        """
        This is the derived function: f(x)' = -sin(x) - 3*x^2
        """
        return -math.sin(x) - 3 * x ** 2

    newton_method(0.5, 6, function_original, function_derived)
