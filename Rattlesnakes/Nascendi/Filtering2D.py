from scipy.ndimage import convolve
from skimage import data
import numpy as np
import matplotlib.pyplot as plt

# Load an example image
image = np.zeros((128, 128))
_eddie = lambda δ, ζ: np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                                [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                                [0, δ, 1, 0, 0, 1, δ, δ, 1, 0, 0],
                                [0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                                [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                                [0, 0, 1, ζ, 1, 1, 1, ζ, 1, 0, 0],
                                [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                                [0, 0, 0, 1, δ, δ, δ, 1, 0, 0, 0],
                                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

## Eddie's random location
from random import randint; ri = lambda x: randint(0, x)

δ, ζ = 1, 0
eddie = _eddie(δ, ζ)
w, u = eddie.shape; v, z = image.shape

δ, ζ = 0, 1
freddy = _eddie(δ, ζ)
for _ in range(4):
   ## Freddy's random locations
   x, y = ri(v - w), ri(z - u)
   image[x:x + w, y:y + u] = np.clip(image[x:x + w, y:y + u] + freddy, 0, 1)

x, y = ri(v - w), ri(z - u)
image[x:x + w, y:y + u] = np.clip(image[x:x + w, y:y + u] + eddie, 0, 1)


# Apply the filter to the image (a.k.a. find smiling Eddie!)
filtered_image = convolve(image, freddy)
skull_location = np.unravel_index(np.argmax(filtered_image, axis = None), filtered_image.shape)
# Pinpoint Eddie's location
filtered_image[skull_location] = 0
# Display the original and filtered images
fig, axes = plt.subplots(1, 2, figsize = (10, 5))
ax = axes.ravel()

ax[0].imshow(image, cmap = plt.cm.copper)
ax[0].set_title('Original Image')

ax[1].imshow(filtered_image, cmap = plt.cm.copper)
ax[1].set_title('Filtered Image')

for a in ax:
   a.axis('off')

plt.title(f'Gotcha@{skull_location}!')
plt.tight_layout()
plt.show()
