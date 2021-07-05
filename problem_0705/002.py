#!/usr/bin/python

import math
import sys  #sys는 바깥에 아규먼트가 있으면 그걸 실행 시키는 역할을 한다.

if len(sys.argv) !=2:
    print(f'#usage:python{sys.argv[0]}[num]') 
    sys.exit()

r=int(sys.argv[1])
pi=math.pi
result=round(r**2*pi,2)

print(result)
