#!/usr/bin/python
fname = "sql.txt"
with open(fname) as f:
    content = f.read().splitlines()
#print content
line = content[0]
caracteres = ['decode(',')']
for i in caracteres:
   line = line.replace(i,'')

par = line.split(',')

sql = (
"(CASE WHEN %s = %s THEN %s"
     "WHEN %s = %s THEN %s END)" 
% (par[0],par[1],par[2],par[0],par[3],par[4])
)

print sql
