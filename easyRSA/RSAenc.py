#coding:utf-8


#实现RSA解密
from Crypto.Util.number import *

m=123456 #明文
e=65537  #一般是这个值
p,q=getPrime(128),getPrime(128) #随机生成两个128位的素数
n=p*q
c=pow(m,e,n) # 加密函数，m的e次方模n，c为密文
print"p=",p
print"q=",q
print"c=",c