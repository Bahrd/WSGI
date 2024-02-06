import numpy as np
import matplotlib.pyplot as plt

from math import isclose, pi as π

'''
"How about a magic trick?" [R+]  https://youtu.be/5K3E5tLoado?t=17
"We make'em dissapear!"    [R++] https://youtu.be/hKzb5YtIz2I
'''

for N in range(9, 11):
    x = np.linspace(0, 2*π, N, endpoint = False)
    s, c = np.sin(x), np.cos(x)
    _ = plt.plot(x, s), plt.plot(x, c), plt.show()

    dp = np.dot(s, c)
    print(f'sgn({dp}) is {np.sign(dp)}, but dp == 0.0 is {isclose(dp, 0.0, abs_tol = 10e-12)}')

