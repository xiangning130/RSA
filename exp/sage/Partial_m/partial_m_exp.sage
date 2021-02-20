e = 0x3
b=0x666c6167206973203a746573743132313131313131313131313133343536000000000000000000
n = 0xf85539597ee444f3fcad07142ecf6eaae5320301244a7cedc50b2beed7e60ffa11ccf28c1a590fb81346fb16b0cecd046a1f63f0bf93185c109b8c93068ec02f
c=0xa75c3c8a19ed9c911d851917e442a8e7b425e4b7f92205ca532a2ab0f5abe6cb86d164cc61374877f9e88e7bca606b43c79f1d59deadfcc68c3db52e5fc42f0
kbits=72
PR.<x> = PolynomialRing(Zmod(n)) # 生成一个以x为符号的一元多项式环
f = (x + b)^e-c # 定义求解函数
x0 = f.small_roots(X=2^kbits, beta=1)[0] # 一个列表，表示所有根
print("x: %s" %hex(int(x0)))