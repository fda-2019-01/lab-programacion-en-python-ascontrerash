##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
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
    maxi=0
    mini=999999
    for row in data:
        if row[0] == t and int(row[1]) > int(maxi):
            maxi=row[1]
        elif row[0] == t and int(row[1]) < int(mini):
            mini=row[1]
    print(t + "," + str(maxi)+","+str(mini))
