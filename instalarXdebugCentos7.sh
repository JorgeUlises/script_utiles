#!/bin/bash
wget http://xdebug.org/files/xdebug-2.4.0.tgz
tar -xvzf xdebug-*
cd xdebug-*
yum install -y php-devel
phpize
./configure
make
cp modules/xdebug.so /usr/lib64/php/modules
cat <<'EOF' > /etc/php.ini
zend_extension = /usr/lib64/php/modules/xdebug.so
EOF
echo Xdebug instalado
