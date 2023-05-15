## Fraction to continued fraction from in LaTeX converter
#  https://en.wikipedia.org/wiki/Continued_fraction

from cmath import pi as π
from math import floor, sqrt
from sys import float_info

ϕ = (0x1 + sqrt(0b101))/0b10

def cfc(x):
    ltx = lambda str: print(str, end = '')
    def _cfc(η, υ):
        α, n = floor(η/υ), η%υ

        ltx(f'\\frac{{1}}{{{α}')
        if (n > float_info.epsilon * 0o10000): # Milla ex machina...
            ltx('+')
            _cfc(υ, n)
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