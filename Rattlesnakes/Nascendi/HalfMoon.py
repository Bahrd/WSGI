from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

# Generate a halfmoon dataset
X, y = make_moons(n_samples = 0x200, noise = .2, random_state = 0o200)

# Visualize the dataset
plt.scatter(X[:, 0], X[:, 1], c = y, cmap = 'viridis')
plt.title('Halfmoon Dataset')
plt.show()


from numpy import array, linspace, dot, sin, cos, pi as π
import matplotlib.pyplot as plt

f, samples = 0x4, 0x40

c, s = (array([cos(f*x) for x in linspace(-π, π, samples)]), 
        array([sin(x) for x in linspace(-π, π, samples)]))
# Is this the real zero? Or just a numerical error?
print(f'{dot(c, s):2.10f}')

plt.plot(linspace(-π, π, samples), c, 'r', label = 'cos(x)')
plt.plot(linspace(-π, π, samples), s, 'k', label = 'sin(x)')
plt.show()



# Something fishy in these waves... 
_c, c_ = (array([cos(x) for x in linspace(-π, π, samples)]), 
          array([cos(f*x) for x in linspace(-π, π, samples)]))
print(f'{_c@c_:2.10f}')

plt.plot(linspace(-π, π, samples), _c, 'r', label = 'cos(x)')
plt.plot(linspace(-π, π, samples), c_, 'k', label = f'cos({f}x)')
plt.show()
