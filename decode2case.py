#!/usr/bin/python

# Auto pep8: autopep8 --in-place --aggressive --aggressive

def findComma(line):
    fin = ''
    if line.find('),') > -1 or line.find(') ,') > -1:
        fin = ','
    return fin


def replaceChars(line, caracteres):
    for i in caracteres:
        line = line.replace(i, '')
    return line


def convDecode(line, caracteres):
    fin = findComma(line)
    line = replaceChars(line, caracteres)
    par = line.split(',')
    # print par
    # print dir(par)
    if len(par) == 4:
        sql = (
            "(CASE WHEN %s = %s THEN %s "
            "ELSE %s END)"
            % (par[0], par[1], par[2], par[3])
        )
    elif len(par) == 5:
        sql = (
            "(CASE WHEN %s = %s THEN %s "
            "WHEN %s = %s THEN %s END)"
            % (par[0], par[1], par[2], par[0], par[3], par[4])
        )
    else:
        sql = "(CASE WHEN {} = {} THEN {} "
        for i in range(0, (len(par) - 5) / 2):
            sql += "WHEN {} = {} THEN {} "
        lista = []
        for i in range(1, ((len(par) - 1) / 2) + 1):
            lista.extend([par[0], par[(i * 2) - 1], par[i * 2]])
        # print lista
        if len(par) % 2 == 0:  # par
            lista.extend([par[len(par) - 1]])
            # print lista
            sql += "WHEN {} = {} THEN {} ELSE {} END)" + fin
        else:
            sql += "WHEN {} = {} THEN {} END)" + fin
        # print lista
        # print sql
        # print len(lista)
        # print len(sql.split("{}"))-1
        sql = sql.format(*lista)
    print sql


def convNVL(line, caracteres):
    fin = findComma(line)
    line = replaceChars(line, caracteres)
    par = line.split(',')
    if len(par) == 2:
        sql = (
            "COALESCE(%s,%s)"
            % (par[0], par[1])
        )
        sql += fin
    print sql


def convLPAD(line, caracteres):
    fin = findComma(line)
    line = replaceChars(line, caracteres)
    par = line.split(',')
    if len(par) == 3:
        sql = (
            "LPAD(CAST(%s AS TEXT),%s,'%s')"
            % (par[0], par[1], par[2])
        )
        sql += fin
    print sql


def convTRIM(line, caracteres):
    fin = findComma(line)
    line = replaceChars(line, caracteres)
    par = line.split(',')
    if len(par) == 3:
        sql = (
            "LPAD(CAST(%s AS TEXT),%s,'%s')"
            % (par[0], par[1], par[2])
        )
        sql += fin
    print sql


def convTO_CHAR(line, caracteres):
    fin = findComma(line)
    line = replaceChars(line, caracteres)
    par = line.split(',')
    if len(par) == 1:
        sql = (
            "CAST(%s AS TEXT)"
            % (par[0])
        )
        sql += fin
    print sql


def convSUBSTR(line, caracteres):
    fin = findComma(line)
    line = replaceChars(line, caracteres)
    par = line.split(',')
    if len(par) == 3:
        sql = (
            "SUBSTR(CAST(%s AS TEXT),%s,%s)"
            % (par[0], par[1], par[2])
        )
        sql += fin
    print sql


def convLENGTH(line, caracteres):
    fin = findComma(line)
    line = replaceChars(line, caracteres)
    par = line.split(',')
    if len(par) == 1:
        sql = (
            "CHARACTER_LENGTH(CAST(%s AS TEXT))"
            % (par[0])
        )
        sql += fin
    print sql

fname = "sql_decode.sql"
with open(fname) as f:
    content = f.read().splitlines()

for line in content:
    if 'DECODE' in line.upper():
        caracteres = ['DECODE(', 'Decode(', 'decode(', ')']
        convDecode(line, caracteres)
    elif 'NVL' in line.upper():
        caracteres = ['NVL(', 'Nvl(', 'nvl(', ')']
        convNVL(line, caracteres)
    elif 'LPAD' in line.upper():
        caracteres = ['LPAD(', 'Lpad(', 'lpad(', ')']
        convLPAD(line, caracteres)
    elif 'TO_CHAR' in line.upper():
        caracteres = ['TO_CHAR(', 'To_char(', 'to_char(', ')']
        convTO_CHAR(line, caracteres)
    elif 'SUBSTR' in line.upper():
        caracteres = ['SUBSTR(', 'Substr(', 'substr(', ')']
        convSUBSTR(line, caracteres)
    elif 'LENGTH' in line.upper():
        caracteres = ['LENGTH(', 'Length(', 'length(', ')']
        convLENGTH(line, caracteres)
    else:
        print "No more lines"
