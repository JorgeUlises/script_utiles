#!/usr/bin/python
def findComma(line):
    fin = ''
    if line.find('),') > -1 or line.find(') ,') > -1:
        fin = ','
    return fin

def replaceChars(line,caracteres):
    for i in caracteres:
        line = line.replace(i,'')
    return line

def convDecode(line):
    fin = findComma(line)
    caracteres = ['decode(','DECODE(',')']
    line = replaceChars(line,caracteres)
    par = line.split(',')
    #print par
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
        lista = []
        for i in range(1,((len(par)-1)/2)+1):
            lista.extend([par[0],par[(i*2)-1],par[i*2]])
        #print lista
        #print ((len(par)- 5)/2)<len(par)
        if ((len(par)- 5)/2)<len(par):
            lista.extend([par[len(par)-1]])
            #print lista
            sql += "WHEN {} = {} THEN {} ELSE {} END)" + fin
        else:
            sql += "WHEN {} = {} THEN {} END)" + fin
        #print lista
        #print sql
        #print len(lista)
        #print len(sql.split("{}"))-1
        sql = sql.format(*lista)
    print sql

def convNVL(line):
    caracteres = ['nvl(','NVL(',')']
    fin	= findComma(line)
    line = replaceChars(line,caracteres)
    par = line.split(',')
    if len(par)==2:
        sql = (
            "COALESCE(%s,%s)"  
            % (par[0],par[1])
        )
       	sql += fin
    print sql

fname = "sql.txt"
with open(fname) as f:
    content = f.read().splitlines()

for line in content:
    if 'DECODE' in line or 'Decode' in line or 'decode' in line:
        convDecode(line)
    else:
        convNVL(line)
