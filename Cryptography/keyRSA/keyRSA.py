from pwn import *
import gmpy2
from gmpy2 import mpz, mpq, mpfr

target = remote("103.245.249.76", 49160)

target.sendafter(": ) ", "y".encode())
target.recvline()
mess = target.recvline()
print(mess.decode())
target.recvline()


paramE = target.recvline(keepends=False)
e = paramE.decode().split(" = ")[1]
print("e = ", e)

paramN = target.recvline(keepends=False)
n = paramN.decode().split(" = ")[1]
print("n = ", n)

paramX = target.recvline(keepends=False)
x = paramX.decode().split(" = ")[1]
print("x = ", x)

out = target.recvline(keepends=False)
print(out.decode())

p = int(x)
q = int(n) // p
phi=(p-1)*(q-1)

x, y = 0, 1

def gcdExtended(a, b):
    global x, y

    if (a == 0):
        x = 0
        y = 1
        return b
 
    gcd = gcdExtended(b % a, a)
    x1 = x
    y1 = y

    x = y1 - (b // a) * x1
    y = x1
    return gcd
    
def modInverse(a, m):
    g = gcdExtended(a, m)
    if (g != 1):
        print("Inverse doesn't exist")
    else:
        res = (x % m + m) % m
        return res

print("phin = ", phi)

d = modInverse(int(e), int(phi))

alpha = math.lcm(p-1, q-1)
value = d + alpha

target.send(str(value).encode())

output = target.recvall()
print(output)
