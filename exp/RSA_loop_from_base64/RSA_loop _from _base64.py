from Crypto.PublicKey import RSA
import gmpy2,libnum

msg='''
eER0JNIcZYx/t+7lnRvv8s8zyMw8dYspZlne0MQUatQNcnDL/wnHtkAoNdCalQkpcbnZeAz4qeMX
5GBmsO+BXyAKDueMA4uy3fw2k/dqFSsZFiB7I9M0oEkqUja52IMpkGDJ2eXGj9WHe4mqkniIayS4
2o4p9b0Qlz754qqRgkuaKzPWkZPKynULAtFXF39zm6dPI/jUA2BEo5WBoPzsCzwRmdr6QmJXTsau
5BAQC5qdIkmCNq7+NLY1fjOmSEF/W+mdQvcwYPbe2zezroCiLiPNZnoABfmPbWAcASVU6M0YxvnX
sh2YjkyLFf4cJSgroM3Aw4fVz3PPSsAQyCFKBA==
'''.decode('base64')
rsa=RSA.importKey(open('prikey.pem','r').read())
n=rsa.n
d=rsa.d
c=libnum.s2n(msg)
for i in range(30):
  m=pow(c,d,n)
  if 'flag' in libnum.n2s(m):
    print libnum.n2s(m)
    break
  c=m