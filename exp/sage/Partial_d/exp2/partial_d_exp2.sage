def partial_p(p0, kbits, n):
    PR.<x> = PolynomialRing(Zmod(n))
    nbits = n.nbits()

    f = 2^kbits*x + p0
    f = f.monic()
    roots = f.small_roots(X=2^(nbits//2-kbits), beta=0.3)  # find root < 2^(nbits//2-kbits) with factor >= n^0.3
    if roots:
        x0 = roots[0]
        p = gcd(2^kbits*x0 + p0, n)
        return ZZ(p)

def find_p(d0, kbits, e, n):
    X = var('X')

    for k in range(1, e+1):
        results = solve_mod([e*d0*X - k*X*(n-X+1) + k*n == X], 2^kbits)
        for x in results:
            p0 = ZZ(x[0])
            p = partial_p(p0, kbits, n)
            if p:
                return p


if __name__ == '__main__':
    n = 0x56a8f8cbc72ff68e67c72718bd16d7e98150aea08780f6c4f532d20ca3c92a0fb07c959e008cbcbeac744854bc4203eb9b2996e9cf630133bc38952a2c17c27d 
    e = 0x3
    d = 0x594b6c9631c4987f588399f22466b51fc48ed449b8aae0309b5736ef0b741893
    beta = 0.5
    epsilon = beta^2/7

    nbits = n.nbits()
    kbits = 255
    d0 = d & (2^kbits-1)
    print("lower %d bits (of %d bits) is given" % (kbits, nbits))

    p = find_p(d0, kbits, e, n)
    print("found p: %d" % p)
    q = n//p
    print("d的低位为：",hex(d))
    print("完整的d为：",hex(inverse_mod(e, (p-1)*(q-1))))