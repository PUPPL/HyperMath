import random as rd
from math import *
from Prime import MillerRabinTest
def GCD(A,B):
    while B != 0:
        t =A%B
        (A,B) = (B,t)
    return abs(A)
def FermatFact(N):
    if N<=0:
        return [N]
    if N%2==0:
        return [N//2, 2]
    a=ceil(sqrt(N))
    if a**2 == N:
        return [a,a]
    while True:
        b1=a**2-N
        b=int(sqrt(b1))
        if b**2==b1:
            break
        else:
            a+=1
    return [a-b,a+b]
def PollardRho(N):
    g = lambda f: (f**2)%N
    if N == 25:
        return 5
    x = rd.randint(2,N-1)
    y = x
    x, y = g(x), g(g(y))
    d = GCD(abs(x-y),N)
    if d != 1:
        return [d,N//d]
    while d==1:
        d = GCD(abs(x-y),N)
        x, y = g(x), g(g(y))
    return [d,N//d]
import cython as c
import time
def fact(N):
    a=1
    for i in range(1, N):
        a*=i
    return a
def cfact(N):
    a=c.longlong(1)
    for i in range(1,N):
        a*= i
    return a

start=time.time()
print(fact(100000))
end=time.time()
print(end-start)
