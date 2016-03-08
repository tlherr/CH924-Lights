# Lights
Python Raspberry Pi Software to control coin operated lighting system


## Installation

Using Raspbian Jessie Lite (Kernel 4.1) Linux raspberrypi 4.1.13-v7+ #826 SMP PREEMPT Fri Nov 13 20:19:03 GMT 2015 armv7l GNU/Linux

Install git
```bash
sudo apt-get install git
```

Clone Source
```bash
git clone https://github.com/tlherr/CH924-Lights.git
```

```bash
cd CH924-Lights
chmod +x dependencies.sh
./dependencies.sh
python main.py
```

## Usage

To run the application simply run:
```bash
python main.py
```

or use cron to automatically start on boot:
```bash
@reboot sh /home/pi/CH924-Lights/run.sh >/home/pi/logs/lights 2>&1
```

To View the WebUI simply visit:

http://raspberrypiipaddress:8000/admin

API endpoints can be called from

http://raspberrypiipaddress:8000/api

## Run on startup

```bash
crontab -e
```

Insert the following:

```
@reboot sh /home/pi/CH924-Lights/run.sh >/home/pi/logs/lights 2>&1
```

This will run the script on system boot and log the output to /home/pi/logs/lights

## Debugging

If for any reason the webserver crashes a debug log will be generated in the project directory


## Wiring

Below is a diagram of the coin machine wiring:

10K resistor used

![diagram](http://fritzing.org/media/fritzing-repo/projects/c/ch924-coin-operated-lights/images/CH924_bb.png "Wiring")