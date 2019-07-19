##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
data = open('data.csv', 'r').readlines()
data = [line[:-1] for line in data]
data = [line.replace('\t', ';') for line in data]
data = [row.split(';') for row in data]
data = [[row[4]] for row in data]
data = ','.join([','.join(line) for line in data]).split(',')
data = [line[:-2] for line in data]
term = sorted(set(data))
for t in term:
    suma=0
    for row in data:
        if row == t:
            suma+=1
    print(t+","+str(suma))
