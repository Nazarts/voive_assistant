#!/bin/bash
#
# A bash script for installing Python 3.7.2 on your Debian, Ubuntu or Mint server.
# Open your terminal and enter the following command:
# wget https://gist.github.com/vbe0201/b85ec47bc198d1c8471acbf016922005/raw/get-python.sh && chmod +x get-python.sh && ./get-python.sh

apt update -y
apt upgrade

sudo apt-get install build-essential checkinstall libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev -y

mkdir python_installation && cd python_installation

wget https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tgz
tar xzvf Python-3.8.12.tgz
rm -f Python-3.8.12.tgz

cd Python-3.8.12

./configure --enable-optimizations
make -j 4
make altinstall

cd ../..
rm -rf python_installation

apt --purge remove build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev -y
apt autoremove -y
apt clean

sudo apt install python3-pip

python3.8 -m pip install -U pip

update-alternatives --install /usr/bin/python python /usr/local/bin/python3.8

sudo update-alternatives  --set python /usr/local/bin/python3.8

echo '$alias pip3="python3.8 -m pip"' >> ~/.bashrc

# Requirements installation

pip install -r requirements.txt