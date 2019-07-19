##
## Imprima la suma de la segunda columna.
##
data = open('data.csv', 'r').readlines()
data = [line[:-1] for line in data]
data = [line.replace('\t', ',') for line in data]
data = [line.replace(':', ',') for line in data]
data = [line.replace(' ', ',') for line in data]
data = [row.split(',') for row in data]
suma=0
for row in data:
    suma = suma + int(row[1])
print(suma)
