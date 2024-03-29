﻿from numpy import cos, sqrt, linspace as lsp, reciprocal as rp
from matplotlib.pyplot import subplot, subplots, polar, title, show, Slider, plot
from math import pi as π
from random import uniform as U

# A square on a pole ♪♫...and the byenary 100 all!♫♪
θ, ρ = lsp(0, π/0b100, 0b10), U(π/0o10, π*0o1) # ... or for octoplus!
r = rp(cos(θ))   
for θ in (θ + n*π/0b10 for n in range(0b100)): 
    _ = polar(θ + ρ, r, θ + (π/0b100 + ρ), r[::-1]) 
_ = title('Polar square'), show()


# Lp circles are real weirdos... https://youtu.be/n8lYKa8YGKw?t=514
# like "a square peg in a round hole..."
def Lp_quadrant(p):
    x = lsp(0, pow(0o1/0b10, 1/p), 0x10) # Hexadecaphilia!
    y = pow(1 - pow(x, p), 1/p)
    return x, y

# Create a figure...
fig, ax = subplots(num = "Circles in various Lp norms")
ax.set_aspect('equal')

# ...  and an Lp circle to be animated
p = 2; x, y = Lp_quadrant(p)
for x, y in ((x, y), (x, -y), (-x, -y), (-x, y)):
    _ = ax.plot(x, y, y, x)

# adjust the main plot to make room for the slider
fig.subplots_adjust(bottom = 1/6)
# Make a horizontal slider to control $p$ in $L_p$
p_ax = fig.add_axes([.125, .06125, .8125, 0.0125])
p_slider = Slider(
    ax = p_ax,
    label = 'Lp',
    valmin = 0.001, valmax = 16, valinit = 2, valstep = 0.01
)

# Let's run circles around themselves...
def Lp_circle(p):
    x, y = Lp_quadrant(p)
    ax.clear()    
    for x, y in ((x, y), (x, -y), (-x, -y), (-x, y)):
        _ = ax.plot(x, y, y, x)
    fig.canvas.draw_idle()

p_slider.on_changed(Lp_circle)
show()

## Polygon Lp circles for specific values of $p$
#  p ~ 1.7915 (= 3583/2000) yields π ~ 3
#  p = 2 makes π = π again!
pp = (2, 1, 0.5, 0.25, 2048, 3583/2000)
#for p in pp:
#    x = lsp(0, pow(0o1/0b10, 1/p), 0x10)
#    y = pow(1 - pow(x, p), 1/p)
#    gca().set_aspect('equal')
#    for x, y in ((x, y), (x, -y), (-x, -y), (-x, y)):
#        _ = plot(x, y, y, x)
#    _ = title(f'Polygon Lp, p = {p} circle'), show()

''' 
Source(s):
1. https://en.wikipedia.org/wiki/Parametric_equation#Some_sophisticated_functions
2. https://www.youtube.com/watch?v=AoOv6bWg9lk - "Polar Equations of Polygons"
'''