# https://g.co/bard/share/3a07f8ffc86b # Don't trust AI... ;)
# https://math.stackexchange.com/questions/927347/uniform-distribution-over-disk#:~:text=This%20is%20the%20uniform%20distribution%20on%20the%20unit,Y%29%20%3D%20%28A%20cos%20B%2C%20A%20sin%20B%29.
# https://www.youtube.com/watch?v=hhFzJvaY__U

from matplotlib.pyplot import gca, scatter, title, show
from numpy import sqrt, sin, cos, pi as π 
from numpy.random import uniform

## Generate N random points in polar coordinates
N = 1000
r, θ = sqrt(uniform(0, 1, N)), uniform(0, 2*π, N)

#  Note that r is now not uniformly distributed. 
#  In order to get a uniform distribution of points 
#  in the disk one needs a map with a constant Jacobian
#
#       ⌈ (1/(2√r))cosθ	    -√rsinθ ⌉
#    det|                           | = (1/2)cos²θ+(1/2)sin²θ, 
#       ⌊ (1/(2√r))sinθ	     √rcosθ ⌋
#
#  which is quite a famous identity... ;)

# Visualize the points
gca().set_aspect('equal')
scatter(r * cos(θ), r * sin(θ), marker = '.', color = 'r')
title('x = √r⋅cosθ and y = √r⋅sinθ'); show()