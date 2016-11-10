#!/bin/bash
#root privileges required
route add default gw 192.168.0.1
route add -net 10.20.0.0 netmask 255.255.0.0 dev ppp0
route add pruebasfuncionarios.intranetoas.udistrital.edu.co dev ppp0
route add pruebasestudiantes.intranetoas.udistrital.edu.co dev ppp0
route add ec2-52-71-252-239.compute-1.amazonaws.com dev ppp0
