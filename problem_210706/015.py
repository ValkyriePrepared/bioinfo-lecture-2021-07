import sys

if len(sys.argv) !=2:
    print(f'python{sys.argv[0]}[sample]')
    sys.exit(1)

sample=sys.argv[1]
print(f'processing: {sample}')
##처리분석
print(f'end:{sample}')
