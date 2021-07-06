s='ATGTTATAG'
s_rev=s[::-1]

'''
print('s:    ',s)
print('s_rev:',s[::-1])
'''

for i in range(len(s)):
    print(f'{s[i]}{s_rev[i]}')
