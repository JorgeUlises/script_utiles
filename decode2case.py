#!/usr/bin/python
def convertir(line):
    for i in caracteres:
       line = line.replace(i,'')
    par = line.split(',')
    #print dir(par)
    if len(par)<=5:
        sql = (
            "(CASE WHEN %s = %s THEN %s"
                  "WHEN %s = %s THEN %s END)" 
            % (par[0],par[1],par[2],par[0],par[3],par[4])
        )
    else:
        sql = "(CASE WHEN {} = {} THEN {} " 
        for i in range(0,(len(par)- 5)/2):
            sql += "WHEN {} = {} THEN {} "
        sql += "WHEN {} = {} THEN {} END)"
        lista = []
        for i in range(1,((len(par)-1)/2)+1):
            lista.extend([par[0],par[(i*2)-1],par[i*2]])
        #print lista
        #print sql
        #print len(lista)
        #print len(sql.split("{}"))-1
        sql = sql.format(*lista)
    print sql

fname = "sql.txt"
caracteres = ['decode(','DECODE(',')']
with open(fname) as f:
    content = f.read().splitlines()

for line in content:
    convertir(line)

