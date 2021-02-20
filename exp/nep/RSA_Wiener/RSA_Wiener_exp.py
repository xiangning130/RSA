from Crypto.Util.number import *

n = 101991809777553253470276751399264740131157682329252673501792154507006158434432009141995367241962525705950046253400188884658262496534706438791515071885860897552736656899566915731297225817250639873643376310103992170646906557242832893914902053581087502512787303322747780420210884852166586717636559058152544979471
e = 46731919563265721307105180410302518676676135509737992912625092976849075262192092549323082367518264378630543338219025744820916471913696072050291990620486581719410354385121760761374229374847695148230596005409978383369740305816082770283909611956355972181848077519920922059268376958811713365106925235218265173085

c = 31471911436392066749733864010956698151523554266700987888625582816064212377168209437878356623985536944755441800836671989921710417329537234931716369096868137364391122900223328337630538782651596115228205049987120939922435307277604076466409854193943345539960814725172950180935238408840597625818779205259900895231

def rational_to_contfrac(x, y):
    a = x//y
    pquotients = [a]
    while a * y != x:
        x, y = y, x-a*y
        a = x//y
        pquotients.append(a)
    return pquotients


def convergents_from_contfrac(frac):
    convs = []
    for i in range(len(frac)):
        convs.append(contfrac_to_rational(frac[0:i]))
    return convs


def contfrac_to_rational(frac):
    if len(frac) == 0:
        return (0, 1)
    num = frac[-1]
    denom = 1
    for _ in range(-2, -len(frac)-1, -1):
        num, denom = frac[_]*num+denom, num
    return (num, denom)


def bitlength(x):
    assert x >= 0
    n = 0
    while x > 0:
        n = n+1
        x = x >> 1
    return n


def isqrt(n):
    if n < 0:
        raise ValueError('square root not defined for negative numbers')

    if n == 0:
        return 0
    a, b = divmod(bitlength(n), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y


def is_perfect_square(n):
    h = n & 0xF

    if h > 9:
        return -1

    if (h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8):
        t = isqrt(n)
        if t*t == n:
            return t
        else:
            return -1

    return -1


def hack_RSA(e, n):
    frac = rational_to_contfrac(e, n)
    convergents = convergents_from_contfrac(frac)
    for (k, d) in convergents:
        if k != 0 and (e*d-1) % k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            discr = s*s - 4*n
            if(discr >= 0):
                t = is_perfect_square(discr)
                if t != -1 and (s+t) % 2 == 0:
                    print("Hacked! d= ", d)
                    return d


d = hack_RSA(e, n)
m = pow(c, d, n)
print(long_to_bytes(m))
