## See https://www.youtube.com/watch?v=P2ZxxoS5YD0
#      https://clifford.readthedocs.io/en/latest/tutorials/g3-algebra-of-space.html#Applications
#      https://www.youtube.com/watch?v=Idlv83CxP-8
import clifford as clf
from math import sqrt as Γ
''' Warning: Never ignore warnings... ;) '''
import warnings; warnings.filterwarnings('ignore')


def p(a: clf.Cl):
    print(f'{a}\ndual = {a.dual()}\ninverse = {"NO" if a*a == 0 else a.inv()}')

# 
names = ['', 'e0', 'e1', 'e2', 'e01', 'e02', 'e12', 'e012']

P, M, Z = 2, 0, 1
layout, blades = clf.Cl(P, M, Z, names = names)
globals().update(blades)
clf.pretty(precision = 2)

#a = eval('e' + ''.join([f'{a}' for a in range(1, P + M + Z + 1)]))

# Extracting a pseudoscalar... (a P+M+Z-vector)
a = list(blades.values())[-1]
p(a.dual())

# Playing with unit bi-vectors (points in PGA)
a, R = e12, e2 + 2*e0
a = R * a * R
p(R)
p(a)

R = (e01 + e12 + e02) / Γ(2.0)
a = R * a * R
p(R)
p(a)

R = R * R
p(R)

a = a * a
p(a)
print('łąćóźżćńę')