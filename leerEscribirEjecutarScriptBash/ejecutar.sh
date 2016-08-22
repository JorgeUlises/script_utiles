#!/bin/bash
. utils

while read linea
do
  printc "$linea"   
  eval "$linea"
done < script_prueba.sh
