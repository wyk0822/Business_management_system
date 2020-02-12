#!/usr/bin/env bash
cd ./lib/package/
tar -xzvf Python-3.7.4.tar.gz
cd Python-3.6.6
./configure --prefix=/usr/local/python3
make all
make install
make clean
make distclean
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
