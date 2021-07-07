import sys

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n=int(sys.argv[1])
print(fib(n))







'''
#! /usr/bin/env python

n_pivo=int(input('n_th pivo: '))
l_pivo=[0,1] #n_th pivo: l_pivo[n]
print('len(l_pivo):',len(l_pivo))

#Use list and. append
def pivo(n):
    while len(l_pivo)<n_pivo:
        l_pivo.append(l_pivo[-1]+l_pivo[-2])
    print(l_pivo[-1])
    print(l_pivo)
pivo(n_pivo)

def pivo_r(n):
'''
