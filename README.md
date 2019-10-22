# Yandex translator GUI 
## Python and GTK 3

Яндекс переводчик на языке Python.
Графический интерфейс яндекс-переводчика.
![screenshot](https://github.com/delvin-fil/Yandex-translator-GUI/blob/master/screenshot.png)
### Зависимости
1. **Python 3.6+**
2. Библиотека **pygobject**
3. Библиотека **requests**
### Установка зависимостей
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
## Установка

```
git clone https://github.com/delvin-fil/Yandex-translator-GUI.git
cd Yandex-translator-GUI
chmod +x yatrans-gtk.py
sudo ln -s $PWD/yatrans-gtk.py /usr/local/bin/yatrans-gtk
```

## Привязка переводчика к горячей клавише
> Так как DE/WM существует довольно много, опишу лишь IceWM, Lumina и Gnome

### IceWm
- Открыть файл $HOME/.icewm/keys
- Добавить строку<br> 
	```key "Ctrl+1" yatrans-gtk```
- Перезапусть IceWM<br>
	```Меню >  Выход... > Перезапуск IceWM```

### Lumina
- Меню > Настройки > Настройки рабочего стола > Горячие клавиши > Расширенный редактор
- Добавить строку<br>
	```Control 1 :Exec yatrans-gtk```

### Gmome 3
- Меню > параметры системы > клавиатура > комбинации клавиш