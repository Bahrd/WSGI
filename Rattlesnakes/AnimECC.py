from matplotlib.pyplot import show, contour, subplots, subplot, title
from numpy import meshgrid, linspace as lp
from matplotlib.widgets import Slider
from numpy.random import randint
# Create an elliptic curve
y, x = meshgrid(lp(-3, 3, 0x200), lp(-3, 3, 0x200))
a, b, c = 0, 0, 0
z = x**3 + a*x**2 + b*x + c - y**2

fig, dx = subplots(num = 'Elliptic curve demo x³ + ax² + bx¹ + cx⁰ = y³')
dx.set_xlabel('X'), dx.set_ylabel('Y')
dx.contour(x, y, z, [0])
title(f'x³ = y³')
    
# adjust the main plot to make room for the sliders
fig.subplots_adjust(left = 1/5, bottom = 1/6)
# Make sliders to control a, b, and c
_sp_ = (([0.25, 0.06125, 0.6125, 0.0125], 'a', 'horizontal'),
        ([0.06125, 0.25, 0.0125, 0.6125], 'b', 'vertical'),
        ([0.93875, 0.25, 0.0125, 0.6125], 'c', 'vertical'))
x_slider, y_slider, z_slider = (Slider(ax = fig.add_axes(_a), label = _l, orientation = _o,
                                       valmin = -3, valmax = 3, valinit = 0, valstep = .1)
                                for _a, _l, _o in _sp_)
# Real curves...
def update(_):
    global a, b, c, x, y
    a, b, c = x_slider.val, y_slider.val, z_slider.val
    z = x**3 + a*x**2 + b*x + c - y**2
    dx.cla()

    cc = f'#{randint(100):02}{randint(100):02}{randint(100):02}'
    contour(x, y, z, [0], colors = cc)
    
    # Anonymous poly-formatting 
    sg = lambda a: '+' if a > 0 else '—'
    ao = lambda a, _: f'{abs(round(a) if round(a, 0) == round(a, 1) else round(a, 1))}' if abs(a) != 1 else '' if _ != '' else '1'
    dsp = lambda a, _: f'{ sg(a)} {ao(a, _)}{_}' if a else '' 
    title(f'x³ {dsp(a, "x²")}{dsp(b, "x")}{dsp(c, "")} = y³')

# register the update function with each slider
x_slider.on_changed(update), y_slider.on_changed(update), z_slider.on_changed(update)
subplot(1, 1, 1); show() #... must go on!
