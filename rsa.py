#!/usr/bin/python3

import math
import gmpy2

n = 10142789312725007
print(math.sqrt(n))
print(repr(math.sqrt(n)))

c = 100711413
for i in range(c, c-40, -2) :
	print(i, n % i)
	
p = 100711409
q = n / p
print(p, q, n, p*q, n - p*q)

phin = (p - 1)*(q - 1)
print(p, q, n, phin)

e = 5
e_mpz = gmpy2.mpz(e)
phin_mpz = gmpy2.mpz(phin)
d = gmpy2.invert(e_mpz, phin_mpz)

#print(d, e, d*e % phin)

x1 = ord("H")
x2 = ord("i")
x3 = ord("!")
x = x1*256*256 + x2*256 + x3
y = x ** e % n
xx = pow(y, d, n)
print(xx)

xx1 = int(xx / (256*256))
xx2 = int((xx - 256*256*xx1) / 256)
xx3 = int(xx - 256*256*xx1 - 256*xx2)
msg = chr(xx1) + chr(xx2) + chr(xx3)

print(xx1, xx2, xx3, msg)

