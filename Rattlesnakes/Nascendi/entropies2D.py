import numpy as np

P = np.array([[1/8,  1/16, 1/32, 1/32],
              [1/16,  1/8, 1/32, 1/32],
              [1/16, 1/16, 1/16, 1/16],
              [1/4,     0,    0,    0]])

def entropy(p, q):
    h = np.sum((-p[p != 0]) * np.log2(q[q != 0]))
    return h

for n in range(len(P)):
    print(P[n, :])
    print(entropy(P[n, :], P[n, :]))
