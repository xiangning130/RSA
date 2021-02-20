from Crypto.Util.number import *

flag = b'xxxx'  # flag=b'flag{xxxxxxx}'
m = bytes_to_long(flag)
e = 65537
p, q = getPrime(128), getPrime(128)
n = p*q
c = pow(m, e, n)
print("c =", c)
print("n =", n)
#c = 19651825676825272901706519046697512456120765226141019655352578091638580547609
#n = 51840578590768198064476632347537981310574396205964652223592866455057467457403
