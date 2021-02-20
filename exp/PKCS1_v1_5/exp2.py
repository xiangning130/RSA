#coding:utf-8
import gmpy2
from gmpy2 import *
from Crypto import *
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import *
import base64


q= 184333227921154992916659782580114145999
p= 336771668019607304680919844592337860739
e= 9850747023606211927
flag_encode=b64decode(open('flag.enc','r').read())
i=1
     
while True:
	print i
	i=i+1
	n = p * q
	d = invert(e,(p-1)*(q-1))
	if n >= int(flag_encode.encode('hex'),16):
			print(p)
			private_key = RSA.construct((int(n),int(e),int(d)))
			cipher = PKCS1_v1_5.new(private_key)
			message = cipher.decrypt(flag_encode,None)
			print(message)
			break
            
	else:
		p = next_prime(p**2 + q**2)
		q = next_prime(2*p*q)
		e = next_prime(e**2)