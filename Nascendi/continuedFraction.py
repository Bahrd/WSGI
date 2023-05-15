## Fraction to continued fraction from in LaTeX converter
#  https://en.wikipedia.org/wiki/Continued_fraction

from cmath import pi as π
from math import floor, sqrt
from sys import float_info

ϕ = (1 + sqrt(5))/2

def cfc(x):
    ltx = lambda str: print(str, end = '')
    def _cfc(N0, N1):
        an, N = floor(N0/N1), N0%N1

        ltx(f'\\frac{{1}}{{{an}')
        if (N > float_info.epsilon * 1000): # At hoc Deus ex machina...
            ltx('+')
            _cfc(N1, N)
        ltx('}')

    ltx(f'{x} = ')
    n = floor(x)
    if(n != 0.0):
        ltx(f'{n}+')
    _cfc(1, x - n)

# Go4π!
cfc(floor(π * 1000)/1000)
# ... and 4gold!
cfc(floor(ϕ * 1000)/1000)
# ... and 4 π = 3 
cfc((2000 + 1583)/2000)