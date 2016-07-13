#!/bin/bash
directorio=/usr/local/apache/htdocs/appserv/fun_fotos/thumbnails
mkdir -p $directorio
cd $directorio
cp ../*.jpg .
mogrify -resize 64x64 *.jpg
