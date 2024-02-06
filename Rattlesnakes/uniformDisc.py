# https://g.co/bard/share/3a07f8ffc86b # Don't trust AI... ;)
# https://math.stackexchange.com/questions/927347/uniform-distribution-over-disk#:~:text=This%20is%20the%20uniform%20distribution%20on%20the%20unit,Y%29%20%3D%20%28A%20cos%20B%2C%20A%20sin%20B%29.
# https://www.youtube.com/watch?v=hhFzJvaY__U

from matplotlib.pyplot import gca, scatter, title, show
from numpy import sqrt, sin, cos, pi as π 
from numpy.random import uniform as U

N = 1000
## Generate N random points in polar coordinates
R, θ = sqrt(U(0, 1, N)), U(0, 2*π, N)

# Displaying the motley points
gca().set_aspect('equal'); title('X = √R⋅cosθ and Y = √R⋅sinθ')
#  Note the square root of R makes the Jacobian of the map constant. 
#  Indeed:
#         ⌈ (1/2√R⋅cosθ  -√R⋅sinθ ⌉
#      det|                       | = 2⁻¹(cos²θ + sin²θ),
#         ⌊ (1/2√R⋅sinθ   √R⋅cosθ ⌋
#
#  is constant by virtue of a quite famous identity... ;)
scatter(R * cos(θ), R * sin(θ), marker = '.', color = 'r'); show()

# Usage (in PowerShell):
# $pyth_on_path = "[...]"
# &$pyth_on_path .\uniformDisc.py