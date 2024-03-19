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

## The first attempt... (to an axiomatic definition of natural numbers)
#  https://en.wikipedia.org/wiki/Set-theoretic_definition_of_natural_numbers
#  - “Aus nichts wird nichts” 
#  - “What are a mathematician’s first words? Hold my paper and watch this.”
_0, _n = '', lambda _: _ + '_' 
f'{_0, _n(_0), _n(_n(_0)), _n(_n(_n(_0))) = } → {len(_0), len(_n(_0)), len(_n(_n(_0))), len(_n(_n(_n(_0))))}'

## ... And the second one:
#_, __, ___ = lambda _, __ : _ + __, [{}], [] 
#f'{len(_(__ , ___)), len(_(__ , (_(__ , ___)))), len(_(__ , ___)) + len(_(__ , (_(__ , ___)))) = }'

## The third time is the charm - as they say...
_0, _n = [], lambda _ : _ + [None]
f'{_0, _n(_0), _n(_n(_0)) = } → {len(_0), len(_n(_0)), len(_n(_n(_0)))}'
