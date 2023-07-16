# Printer cabinet temperature control

## Pre-requisites

### Enabling I2C1 from terminal

```shell
sudo raspi-config
```

Interfacing options > I2C > Enable

```shell
sudo reboot
```

```sh
sudo apt-get -y install git build-essential libgpiod2 python3-dev python3-openssl python3-rpi.gpio python3-pip python3-smbus
```

```shell
pip install -r requirements.txt
```

## How to install

### Install as service

```shell
make install-as-service
```

## Local development 

Create the virtual env

```shell
pyenv virtualenv 3.9.6 printer-cabinet-temperature-control
```

Load the environment

```shell
pyenv local printer-cabinet-temperature-control
```

Install dependencies

```shell
pip install -r requirements.txt
```

## References


### DHT 22 sensor

https://www.instructables.com/Raspberry-Pi-Tutorial-How-to-Use-the-DHT-22/

### I2C LCD 1602

https://raspberrypilife.com/how-to-use-the-i2c-lcd-1602-with-the-raspberry-pi/
https://gist.github.com/DenisFromHR/cc863375a6e19dce359d
