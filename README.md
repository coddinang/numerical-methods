## Numerical Methods

### Root Finding

Solve <img src="https://latex.codecogs.com/gif.latex?f(x)=0"/> for <img src="https://latex.codecogs.com/gif.latex?x"/>, when an explicit analytical solution is imposible.
#### Bisection Method
We want to construct a sequence <img src="https://latex.codecogs.com/gif.latex?x_0" />, <img src="https://latex.codecogs.com/gif.latex?x_1" />, <img src="https://latex.codecogs.com/gif.latex?x_2" />, that converges to the root <img src="https://latex.codecogs.com/gif.latex?x=r" /> that solves <img src="https://latex.codecogs.com/gif.latex?f(x)=0" />. We choose <img src="https://latex.codecogs.com/gif.latex?x_0" /> and <img src="https://latex.codecogs.com/gif.latex?x_1" /> such that <img src="https://latex.codecogs.com/gif.latex?x_0<r<x_1" />. We say that <img src="https://latex.codecogs.com/gif.latex?x_0" /> and <img src="https://latex.codecogs.com/gif.latex?x_1" /> bracket the root. With <img src="https://latex.codecogs.com/gif.latex?f(r)=0" />, we want <img src="https://latex.codecogs.com/gif.latex?f(x_0)" /> and <img src="https://latex.codecogs.com/gif.latex?f(x_1)" /> to be of opposite sign, so that <img src="https://latex.codecogs.com/gif.latex?f(x_0)f(x_1)<0" />. We then assign <img src="https://latex.codecogs.com/gif.latex?x_2" /> to be the midpoint of <img src="https://latex.codecogs.com/gif.latex?x_0" /> and <img src="https://latex.codecogs.com/gif.latex?x_1" />, that is:
<img src="https://latex.codecogs.com/gif.latex?x_2=\frac{x_0+x_1}{2}"/>
or
<img src="https://latex.codecogs.com/gif.latex?x_2=x_0+\frac{x_1-x_0}{2}"/>
