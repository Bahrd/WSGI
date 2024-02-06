# https://github.com/moble/quaternion/tree/main/src/quaternion
import numpy as np
import quaternion
from math import sin, cos, isclose, pi as π

# https://www.youtube.com/watch?v=jTgdKoQv738
def Θ(q: quaternion, r: quaternion):
    return r * q * r.conjugate()/r.norm()

a, b, c = 0.0, 45, 0.0
α, β, γ = np.deg2rad((a, b, c))
rotor, q = (quaternion.from_euler_angles(α, β, γ),
            np.quaternion(0, 1, 0, 0))

print(f"q = {q} has a mon-zero norm {q.abs()} and hence is{' ' if isclose(q.abs(), 1.0) else ' not '}normalized")
print(np.rad2deg(quaternion.as_euler_angles(q)))
print(np.rad2deg(quaternion.as_euler_angles(rotor)))

rq = rotor * q 
print(f'{rotor}*{q} = {rq}')
print(np.rad2deg(quaternion.as_euler_angles(rq)))
rqr = rq * rotor.conjugate()
print(f'sandwiched = {rqr}')
print(np.rad2deg(quaternion.as_euler_angles(rqr)))

rqr = Θ(rqr, rotor.conjugate())
print(f're-sandwiched = {rqr}')
print(np.rad2deg(quaternion.as_euler_angles(rqr)))



'''
qr = quaternion.from_euler_angles(α, β, γ)
print(a, b, c)

a, b, c = 0.0, 45.0, 0.0
α, β, γ = np.deg2rad((a, b, c))
ang = quaternion.from_euler_angles(α, β, γ)
# np.quaternion(0, 0, 1, 0)
#a, b, c = np.rad2deg(quaternion.as_euler_angles(ang))
print(a, b, c)

rq = Θ(ang, qr)

a, b, c = np.rad2deg(quaternion.as_euler_angles(rq))
print(a, b, c)
'''