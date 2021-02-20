p = 0xd7e990dec6585656512c841ac932edaf048184bac5ebf9967000000000000000
n = 0xb50193dc86a450971312d72cc8794a1d3f4977bcd1584a20c31350ac70365644074c0fb50b090f38d39beb366babd784d6555d6de3be54dad3e87a93a703abdd

kbits = 60
PR.<x> = PolynomialRing(Zmod(n))
f = x + p
x0 = f.small_roots(X=2^kbits, beta=0.4)[0]
print("x: %s" %hex(int(x0)))
p = p+x0
print("p: ", hex(int(p)))
assert n % p == 0
q = n/int(p)
print("q: ", hex(int(q)))