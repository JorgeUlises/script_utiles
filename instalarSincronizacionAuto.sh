#!/bin/bash

if [ $USER != "root" ]; then
  echo "El comando debe ser ejecutado como ROOT"
  exit
fi

archivo=/root/.ssh/git_rsa
echo "Instalando $archivo"
cat <<'EOF' > $archivo
-----BEGIN RSA PRIVATE KEY-----
ACA VA LA LLAVE PRIVDA SSH
uTQ7j4BoKM9gOW80SjIFW2poCSiLflVRWhQB3XHz18rOp86bBHHw13IWm6wngGHB
9aNA9HcnIYzX6u85h1wl2U/CUpftJna55gI5O71T+BmhfRs4qPiw
-----END RSA PRIVATE KEY-----
EOF
chmod 400 $archivo

archivo=/root/.ssh/git_rsa.pub
echo "Instalando $archivo"
cat <<'EOF' > $archivo
ssh-rsa AAAAACAVAELCODIGOPRIVADOSSHPcN jorgenator2@yahoo.es
EOF

archivo=/usr/bin/pullestudiantes.sh
echo "Instalando $archivo"
cat <<'EOF' > $archivo
date
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/git_rsa
ssh -T git@github.com
cd /var/www/html
git pull origin master
EOF
chmod +x $archivo

archivo=/etc/cron.d/pullestudiantes
echo "Instalando $archivo"
cat <<'EOF' > $archivo
#00 * * * * root /usr/bin/pullestudiantes.sh 2>&1 | tr '\r\n' ' ' | (cat; echo)  >> /var/log/pullestudiantes.log
* * * * * root /usr/bin/pullestudiantes.sh 2>&1 | tr '\r\n' ' ' | (cat; echo)  >> /var/log/pullestudiantes.log
EOF

echo "Se ha instalado exitosamente"
