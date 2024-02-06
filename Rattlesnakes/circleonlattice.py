'''
It ain't easy to find the area of the circle on a screen...
https://mathworld.wolfram.com/GausssCircleProblem.html

\[
GCA\left(r\right) = 1 + 4\left\lfloor r\right\rfloor 
                      + 4\sum_{i = 0}^{\left\lfloor r\right\rfloor }
                      \left\lfloor \sqrt{r^{2} - i^{2}}\right\rfloor
\]

'''
from numpy import add
from math import floor, sqrt, pi as π
from matplotlib.pyplot import plot, show

def Gauss_circle_area(r: float):
    r_floor = int(floor(r))
    rs = [floor(sqrt(r**2 - i**2)) for i in range(1, r_floor)]
    area = 1 + 4*r_floor + 4*add.reduce(rs)
    return area

print(f'{Gauss_circle_area(10)} sq. pixels vs. {π*10**2:.2f} sq. whatevers')
plot([Gauss_circle_area(r) - π*r**2 for r in range(0x400)], 'r.'), show()
