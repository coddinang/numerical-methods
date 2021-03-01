## Numerical Methods
### Root Finding
Solve $$f(x) = 0 $$ for $$x$$ , when an explicit analytical solution is imposible.
#### Bisection Method
We want to construct a sequence $$x_0$$,$$ x_1$$,$$x_2$$, that converges to the root $$x = r$$ that solves $$f(x) = 0$$. We choose $$x_0$$ and $$x_1$$ such that $$x_0 < r < x_1$$. We say that $$x_0$$ and $$x_1$$ bracket the root. With $$f(r) = 0$$, we want $$f(x_0)$$ and $$f(x_1)$$ to be of opposite sign, so that $$f(x_0)f(x_1) < 0$$. We then assign $$x_2$$ to be the midpoint of $$x_0$$ and $$x_1$$, that is:
$$x_2 = \frac{x_0 + x_1}{2}$$
or
$$x_2 = x_0 + \frac{x_1 - x_0}{2}$$
