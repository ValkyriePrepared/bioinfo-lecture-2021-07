

file_name='read_sample.txt'
'''
with open(file_name,'r')as handle:
    for line in handle:
        print(line.strip()) #여기서 strip을 제거하면 출력시 엔터친게 아니라 붙어서 나온다.
                            #궁금하면 한번 보자 바로 차이를 알 수 있을 것이다.

handle=open(file_name,'r')
for line in handle:
    print(line)    #strip을 제거하고 쳐본거다.
handle.close() #close 를 적어주지 않으면 안된다.
'''

handle=open(file_name,'r')
lines=handle.readlines()
for line in lines:
    print(line.strip())
handle.close()

