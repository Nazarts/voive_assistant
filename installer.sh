#!/bin/bash
#
# A bash script for installing Python 3.7.2 on your Debian, Ubuntu or Mint server.
# Open your terminal and enter the following command:
# wget https://gist.github.com/vbe0201/b85ec47bc198d1c8471acbf016922005/raw/get-python.sh && chmod +x get-python.sh && ./get-python.sh

apt update -y
apt upgrade

sudo apt-get install build-essential checkinstall libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev -y

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt-get update

sudo apt-get install python3.8

sudo apt install python3-pip

python3.8 -m pip install -U pip

# Requirements installation

python3.8 -m pip install -r requirements.txt