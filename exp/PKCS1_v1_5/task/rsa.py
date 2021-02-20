#!/usr/bin/env python3
import gmpy2
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64encode


flag = open('flag', 'r').read().strip() * 23        #flag复制23遍


def encrypt(p, q, e, msg):
    while True:
        n = p * q
        try:
            phi = (p - 1)*(q - 1)
            pubkey = RSA.construct((int(n), int(e)))  #构造公钥
            key = PKCS1_v1_5.new(pubkey)              #利用PKCS1_v1_5进行加密，PKCS1_v1_5是一种利用RSA算法进行的数字签名算法
            enc = b64encode(key.encrypt(msg))         #RSA加密后再进行base64加密
            return enc
        except:                                       #如果加密不成功，变化p、q和e，直到加密成功
            p = gmpy2.next_prime(p**2 + q**2)              
            q = gmpy2.next_prime(2*p*q)
            e = gmpy2.next_prime(e**2)


p = getPrime(128)         
q = getPrime(128)
n = p*q
e = getPrime(64)
pubkey = RSA.construct((n, e))
with open('pubkey.pem', 'wb') as f:
    f.write(pubkey.exportKey())
with open('flag.enc', 'wb') as g:
    g.write(encrypt(p, q, e, flag.encode()))        #复制23遍后的flag带入encrypt中
