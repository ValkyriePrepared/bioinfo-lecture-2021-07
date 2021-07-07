cnt_all=0
cnt_pass=0


with open('070.vcf','r') as handle:
    for line in handle:
        if line.startswith('##'):
            continue
        elif line.startswith('#'):
            header=line.strip().split('\t')
            filter_idx=header.index('FILTER')
            continue
        data=line.strip().split('\t')
        cnt_all+=1
        #if data[6]=='PASS':
        if data[filter_idx]=='PASS':
            cnt_pass+=1
print(cnt_pass,cnt_all,cnt_pass/cnt_all)






'''
result=0
with open('077.bed','r') as handle:
    for line in handle:
        data=line.strip().split('\t')
        # int(data[2])-int(data[1])
        chrom,start,end=data
        length=int(end)-int(start)
        result+=length
print(result)


'''








