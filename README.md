# Yandex translator GUI

Графический интерфейс яндекс-переводчика.

### Зависимости
1. **Python 3.6+**
2. Библиотека **pygobject**
3. Библиотека **requests**
### Установка зависимостей:
#### Ubuntu/Mint/Debian:
```shell
sudo apt-get install python3.6 python3-pip python3-gi python3-gi-cairo gir1.2-gtk-3.0
pip3.6 install --user requests
```
#### CentOS:
```shell
sudo yum install -y https://centos8.iuscommunity.org/ius-release.rpm
sudo yum update
sudo yum install -y python36u python36u-libs python36u-devel python36u-pip
pip3.6 install --user requests
```
#### RedHat:
```shell
su
yum install gcc openssl-devel bzip2-devel sqlite-devel
cd /usr/src
wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz
tar xzf Python-3.6.9.tgz
cd Python-3.6.9
./configure --enable-optimizations
make altinstall
pip3.6 install --user requests
```
#### Gentoo:
```shell
sudo USE="cairo" PYTHON_TARGETS="python2_7 python3_6" emerge dev-python/pygobject -av
pip3.6 install --user requests
```
