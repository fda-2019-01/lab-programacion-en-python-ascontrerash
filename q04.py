##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
data = open('data.csv', 'r').readlines()
data = [line[:-1] for line in data]
data = [line.replace('\t', ',') for line in data]
data = [line.replace(':', ',') for line in data]
data = [line.replace(' ', ',') for line in data]
data = [line.replace('-', ',') for line in data]
data = [row.split(',') for row in data]
meses = [[row[3]] for row in data]
meses = ','.join([','.join(line) for line in meses]).split(',')
term = set(sorted(meses))
for t in sorted(term):
    aux = meses.count(t)
    print(t+","+str(aux))
