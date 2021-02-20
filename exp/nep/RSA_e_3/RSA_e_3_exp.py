from gmpy2 import iroot
from Crypto.Util.number import *

n = 126569890903903596197382665579802884683844555473870845250806495408809907164879564030715035485821669628893163657754942373871206630282074952120186772302981417815134803872001403137071074416677237195900769686708999662508791292439714050928255723554686537941165968533332062722589939546565092416460282667822165913733
c = 36249228279230763252981933571776205501973012164399086661686568369451225056169871361897338240617003359536233973257828125797854483956384044187432738408224816731658424420740324471268926030614272472424841198952096926400204340598267818665095983208618977069824530628197868621507390059816072832075424690714289649266

for k in range(1000):
    if iroot(c+k*n,3)[1]==True:
        m=iroot(c+k*n,3)[0]
        break

flag=long_to_bytes(m)
print(flag)