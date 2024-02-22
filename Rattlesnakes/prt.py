'''
   ♪♫... and the RT 4 all!♫♪ 
   
1. A pinhole camera have no DoF - neither the RT algorithm based on it.
2. However, an image of a pinhole camera captures 'soft shadows'
   created by light source that are not point ones 
   (and not directional ones either). 
3. In the RT algorithms "soft shadows" can be obtained by 
   representing an area light source by a collection of 
   separate (but adjacent) point sources.
'''

## The first attempt... (to axiomatic definition of natural numbers)
_, __, ___ = lambda _, __ : _ + __, [{}], [] 
f'{len(_(__ , ___)), len(_(__ , (_(__ , ___)))), len(_(__ , ___)) + len(_(__ , (_(__ , ___)))) = }'

## The second one...
_0, _n = [], lambda _ : _ + [{}]
f'{len(_0), len(_n(_0)), len(_n(_n(_0))) = }'
