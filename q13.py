##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
data = open('data.csv', 'r').readlines()
data = [line[:-1] for line in data]
data = [line.replace('\t', ';') for line in data]
data = [row.split(';') for row in data]
data = [[row[0],row[4]] for row in data]
for row in data:
    suma=0
    string = row[1]
    for i in range(len(string)):
        if string[i-1]==":":
            suma+=int(string[i])
    print(row[0]+","+str(suma))
