import math

def false_position_method(x_a, x_b, func):
    i = 0
    c_before = 0
    print("| a | b | f(a) | f(b) | c | f(c) |")
    
    while True:
        f_a = func(x_a)
        f_b = func(x_b)
        subs = x_b - x_a
        c = x_a - (subs*f_a/(f_b-f_a))
        f_c = func(c)
        print("| {} | {} | {} | {} | {} | {} |".format(
            round(x_a, 4), round(x_b, 4), round(f_a, 4),
            round(f_b, 4), round(c, 4), round(f_c, 4)))

        if i > 0:
            error = math.fabs((c-c_before)/c)
            if error == 0:
                break

        sig = f_a*f_c
        if sig > 0:
            x_a = c
        elif sig < 0:
            x_b = c
        c_before = c
        i += 1


if __name__ == '__main__':
    a, b = 1, 2

    def math_function(x):
        """
        This is a math function: f(x) = e^-x * (3.2 * sin(x) - 0.5 * cos(x))
        """
        return math.exp(-x) * (3.2 * math.sin(x) - 0.5 * math.cos(x))


    false_position_method(a, b, math_function)
