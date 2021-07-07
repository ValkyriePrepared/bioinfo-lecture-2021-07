file_name='059.fasta'

data=dict()    #딕셔너리 초기화   data={} 이것도 가능

with open(file_name,'r')as handle:
    for line in handle:
        if line.startswith('>'):
            continue
        for base in line.strip():
            if base not in data:
                data[base]=0
            data[base]+=1 

print(data)

