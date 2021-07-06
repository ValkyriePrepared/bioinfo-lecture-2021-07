file_name='write_sample.txt'

handle=open(file_name,'w')
handle.write('Hello\n')
handle.write('Bioinformatics)\n')

with open(file_name,'a')as handle:
    handle.write('ken\n')

s='s1,s2,s3' #csv :콤마로 분리되어 있는 데이터 CSV(Comma-Sparated Values)파일은 각 필드를 쉼표로 구분한다. 기본적으로 텍스트 파일이므로 텍스트 에디터를 사용해 간편하게 수정할 수 있다. TSV(Tab-Sparated Values)파일은 CSV와 비슷하지만 쉼표가 아닌 탭으로 필드를 구분한다.
data=s.split(',')
print(data) #['s1','s2','s3']

with open(file_name,'a')as handle:
    handle.write('\t'.join(data))

