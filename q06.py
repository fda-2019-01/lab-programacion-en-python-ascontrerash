##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
data = open('data.csv', 'r').readlines()
data = [line[:-1] for line in data]
data = [line.replace('\t', ';') for line in data]
data = [row.split(';') for row in data]
data = [[row[4]] for row in data]
data = ','.join([','.join(line) for line in data]).split(',')
#data = [line[:-2] for line in data]
terminos = [line[:-2] for line in data]
term = sorted(set(terminos))
data = [line.replace(':',';') for line in data]
data = [row.split(';') for row in data]
for t in term:
    mini=999999
    maxi=0
    for row in data:
        if t == row[0]:
            if int(row[1])>maxi:
                maxi=int(row[1])
            elif int(row[1])<mini:
                mini=int(row[1])
    print(t+","+str(mini)+","+str(maxi))
