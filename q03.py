##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
data = open('data.csv', 'r').readlines()
data = [line[:-1] for line in data]
data = [line.replace('\t', ',') for line in data]
data = [line.replace(':', ',') for line in data]
data = [line.replace(' ', ',') for line in data]
data = [row.split(',') for row in data]
terminos = [[row[0]] for row in data]
terminos = ','.join([','.join(line) for line in terminos]).split(',')
term = set(sorted(terminos))
for t in sorted(term):
    suma=0
    for row in data:
        if row[0] == t:
            suma = suma + int(row[1])
    print(t + "," + str(suma))
    print(t + "," + str(suma))
