import os
from urllib.request import urlretrieve
u1='https://hub.jovian.ml/wp-content/uploads/2020/08/loans1.txt'

print(os.getcwd())

urlretrieve(u1,'./data/l1.txt')

with open('./data/l1.txt') as fr:
    file_r=fr.readlines()
    print(f"org{file_r}")


    def parse_headers(headerline):
        return headerline.strip().split(',')
    headers=parse_headers(file_r[0])
    print(headers)

    def parse_values(dataline):
        values=[]
        for item in dataline.strip().split(','):
            if item=='':
                values.append(0.0)
            else:
                values.append(float(item))
        print(f'func  {values}')
    n=1
    for x in range(len(file_r)):
        parse = parse_values(file_r[n])
        n+=1
        if n==len(file_r):
            break

    def create_dict(values,headers):
        result={}
        for header,value in zip(values,headers):
            result[headers]=values
        print(result)

    m=1
    for x in range(len(file_r)):
        cd = create_dict(file_r[m],file_r[0])
        m+=1
        if m == len(file_r):
           break







