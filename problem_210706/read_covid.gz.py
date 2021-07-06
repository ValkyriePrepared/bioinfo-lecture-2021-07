import gzip

file_name='covid19.fasta.gz'

data=dict()    #딕셔너리 초기화   data={} 이것도 가능

with gzip.open(file_name,'rt')as handle: #rt: read text  ,  rb:read binary
    for line in handle:
        if line.startswith('>'):
            continue
        for base in line.strip():
            if base not in data:
                data[base]=0
            data[base]+=1
            
print(data)
