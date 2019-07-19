##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
data = open('data.csv', 'r').readlines()
data = [line[:-1] for line in data]
data = [line.replace('\t', ',') for line in data]
data = [line.replace(':', ',') for line in data]
data = [line.replace(' ', ',') for line in data]
terminos = [[row[0]] for row in data]
terminos = ','.join([','.join(line) for line in terminos]).split(',')
term = set(sorted(terminos))
for t in sorted(term):
    aux = terminos.count(t)
    print(t+","+str(aux))
