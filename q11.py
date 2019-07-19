##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
import math
data = open('data.csv', 'r').readlines()
data = [line[:-1] for line in data]
data = [line.replace('\t', ';') for line in data]
data = [row.split(';') for row in data]
data = [[row[0],row[3],row[4]] for row in data]
for row in data:
    aux1=math.ceil((len(row[1]))/2)
    aux2=math.ceil((len(row[2]))/6)
    print(row[0]+","+str(aux1)+","+str(aux2))
