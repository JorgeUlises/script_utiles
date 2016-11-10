#!/bin/bash
#root privileges required
route add default gw 192.168.0.1 #reemplazar por puerta de enlace conexion
route add -net 10.20.0.0 netmask 255.255.0.0 dev ppp0
