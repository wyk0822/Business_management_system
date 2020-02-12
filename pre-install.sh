#!/usr/bin/env bash
# 安装Python
cd ./lib/package/
tar -xzvf Python-3.7.4.tar.gz
tar -xzvf django-1.11.18.tar.gz
tar -xzvf django-simple-captcha-0.5.12.tar.gz


cd Python-3.7.4
./configure --prefix=/usr/local/python3
make all
make install
make clean
make distclean
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3

cd ../
echo $(pwd)
cd django-1.11.18
sudo python3 setup.py install

cd ../
echo $(pwd)
cd django-simple-captcha
sudo python3 setup.py install