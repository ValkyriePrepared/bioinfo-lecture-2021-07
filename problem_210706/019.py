import sys


'''
with open('hahaha.txt','r')as handles:
    data=handle.readlines()

print(data) #hahaha가 없어서 오류가 난다.
'''
try:
    with open('hahaha.txt','r')as handle:
        data=handle.readlines()
except FileNotFoundError as err:
    print('파일이 없다')
    sys.exit()

print(data)
