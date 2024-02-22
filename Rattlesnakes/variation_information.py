from cv2 import imread
from numpy import count_nonzero, any, log2
from matplotlib.pyplot import plot, show, subplot
from sys import argv

def entropy(p):
    p = [x * log2(x) for x in p if x > 0]
    return -sum(p)

## Parameters
filenames =  [f'L{1.0*2**i}' for i in range(-4, 5)]
#shades = [[0x20 + a]*3  for a in range(0x0, 0x100 - 0x20, 0x20)] + [[0x0, 0x0, 0xff]]
c = eval(argv[1]) if len(argv) == 2 else 16
shades = list([int(0x100*(i/c))]*3 for i in range(c))

H = []
for f in filenames:
    img = imread(f + '.png')    
    AM = []
    for shade in shades:
        ### A pixel-counting method
        h, w, _ = img.shape; hxw = h * w    # No. of all pixels

        pixels = count_nonzero(any(img != shade, axis = 2))
        a_m = 1.0 - pixels/hxw 
        AM += [a_m]        

    H += [entropy(AM)]        
    print(f'Entropy for {f} = {entropy(AM):0.3f}')
    
subplot(2, 1, 1); plot(filenames, H, 'r.')

H = []
### A Monte Carlo approach (random sampling)
from numpy.random import default_rng as drng
samples = 0x200*0x200   # No. of all samples
rng = drng()            # Random samples with Numpy 1.17+

for f in filenames:
    img = imread(f + '.png')    
    AM = []
    for shade in shades:
        ## ... and a code
        x, y = rng.integers([h, w], size = [samples, 2]).T
        pixels = count_nonzero(any(img[x, y] != shade, axis = 1))

        a_m = 1.0 - pixels/samples
        AM += [a_m]        

    H += [entropy(AM)]        
    print(f'MC\'s entropy for {f} = {entropy(AM):0.3f}')

subplot(2, 1, 2); plot(filenames, H, 'r.')
show()
