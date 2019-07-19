##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
import re
data = open('data.csv', 'r').readlines()
data = [line[:-1] for line in data]
data = [line.replace('\t', ';') for line in data]
data = [row.split(';') for row in data]
data = [[row[1],row[3]] for row in data]
terminos = [[row[1]] for row in data]
terminos = ','.join([','.join(line) for line in terminos]).split(',')
term = sorted(set(terminos))
term
data
for t in term:
    aux=0
    for row in data:
        if re.search(t, row[1]):
            aux+=int(row[0])
    print(t+","+str(aux))
