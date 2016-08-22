#!/bin/bash
if [ "$DEBUG_MODE" == "true" ]
then
  echo 'DEBUG_MODE es true'
else
  echo 'Intente: DEBUG_MODE=true ./script_prueba.sh'
fi

echo 'Este escript está ejecutando línea por línea'
echo 'Lo que se quiere decir, e imprime el comando'
sleep 1
ls -la ~/ | grep -i bash
touch hi.txt
echo "Hola" > hi.txt
cat hi.txt
tac hi.txt
echo "Qué hay de nuevo viejo" >> hi.txt
cat hi.txt | sed 's/nuevo/viejo/g'
rm hi.txt
