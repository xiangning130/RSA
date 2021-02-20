

# This file was *autogenerated* from the file partial_p_exp.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1024 = Integer(1024); _sage_const_130 = Integer(130); _sage_const_2 = Integer(2); _sage_const_0p4 = RealNumber('0.4'); _sage_const_0 = Integer(0)
n = 0x241ac918f708fff645d3d6e24315e5bb045c02e788c2b7f74b2b83484ce9c0285b6c54d99e2a601a386237d666db2805175e7cc86a733a97aeaab63486133103e30c1dca09741819026bd3ea8d08746d1d38df63c025c1793bdc7e38d194a30b492aadf9e31a6c1240a65db49e061b48f1f2ae949ac9e7e0992ed24f9c01578d   
p_fake = 0x2c1e75652df018588875c7ab60472abf26a234bc1bfc1b685888fb5ded29ab5b93f5105c1e9b46912368e626777a873200000000000000000000000000000000   
   
pbits = _sage_const_1024   
kbits = _sage_const_130   
pbar = p_fake & (_sage_const_2 **pbits-_sage_const_2 **kbits)  
print("upper %d bits (of %d bits) is given" % (pbits-kbits, pbits))
   
PR = PolynomialRing(Zmod(n), names=('x',)); (x,) = PR._first_ngens(1)
f = x + pbar  
   
x0 = f.small_roots(X=_sage_const_2 **kbits, beta=_sage_const_0p4 )[_sage_const_0 ]  # find root < 2^kbits with factor >= n^0.3  
print(hex(int(x0 + pbar)))
