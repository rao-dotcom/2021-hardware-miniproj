# 2021 Hardware Miniproject

Fall 2021 ECE Senior Capstone miniproject

This project will be done in multiple steps.
The first part is the setup of the Raspberry Pi hardware.

The second part is an exercise to gain familiarity with Python and embedded sensors. It will require the Raspberry Pi OS to be working. It will be released Monday, September 6, 2021.

The third part using the Raspberry Pi as a wireless sensor will be released Thursday, September 9, 2021.

## Part 1: setup Raspberry Pi

The Raspberry Pi requires the students obtain a micro-SD card and install the Raspberry Pi OS.
8GB or larger micro SD card recommended--these days, 32 GB is often the minimum size one finds commonly available.
An 32GB micro SD UHS-1 card is about $5 from:

* Microcenter (730 Memorial Drive, Cambridge--just across BU Bridge)
* Amazon
* many other places

The Raspberry Pi OS is a freely available fork of Debian customized for the Raspberry Pi.
To install the OS, the student team will need to
[download the OS image](https://www.raspberrypi.org/software/)
via the installer to the SD card.
Please use care that the installer refers to the path to the SD card.
If your computer doesn't have a micro SD slot, consider buying an inexpensive USB to micro SD adapter or using another computer.

Notes:

* if you have trouble with the laptop crashing while writing or verifying the SD card, try temporarily turning off virus protection, especially on Windows.
* The Raspberry Pi 4 uses more power than prior generations. It might not operate correctly from laptop USB-C. We suggest using the Raspberry Pi 4 AC power adapter for stable power.

We have setup a few HDMI displays and USB keyboards in the senior design lab to share.
Please let us know if we need to add more.

### SSH connection

To connect to the Raspberry Pi over SSH do one of the following.
Be sure to pick a strong password for the Raspberry Pi, or the Pi will quickly become hacked as university networks are aggressively scanned for low security passwords.

* external HDMI display: type "raspi-config" in the terminal, "Interface Options", "SSH" enable.
* no display, via Ethernet cable to laptop: create a blank file named "ssh" in the "boot" partition of the SD card while it's in your laptop. This is done on Linux or MacOS from the "boot" directory by `touch ssh` or on Windows PowerShell by `New-Item ssh`

To connect to the Raspberry Pi over SSH while plugged into the Pi with an Ethernet cable from your laptop, type the following in the terminal:

```sh
ssh pi@raspberrypi.local
```

If you can't connect, ensure your computer is connected to the Raspberry Pi via Ethernet cable directly.
For example, on Windows type "ipconfig" and the response should include:

```
> ipconfig

Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : <hex-address>
   Autoconfiguration IPv4 Address. . : 169.254.57.200
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
   Default Gateway . . . . . . . . . :
```

The last digits will be different, the important part is the "169.254" indicating you have a "link-local" connection active.

If you still can't get it working, use an HDMI display and keyboard to the Pi, which can be easier to get started when there's a connection problem.

### Internet connection

To enable the WiFi internet connection, from "raspi-config", "System Options", "Wireless LAN" setup the WiFi network.
Note that if you choose to use university WiFi, your Kerberos password is visible to anyone with access to the Pi.
So you might want to use an Ethernet cable to the internet or phone hotspot for the Pi.

You can check that the Pi is on the internet by typing in the Pi terminal (over SSH or HDMI+keyboard):

```sh
curl https://ident.me
```

that will give the public IP address of the Pi, if the public internet connection is up.

## Part 2: Python sensor exercise

The commands in this section are all run on the Raspberry Pi, over SSH or HDMI+keyboard.
Let's update the Raspberry Pi OS, as the OS releases only happen a few times a year.

```sh
sudo apt update && sudo apt upgrade
```

Like most Linux systems, the Raspberry Pi comes with Python installed.
Since we're going to be using system hardware drivers, we'll use system Python.
Check that Python is working:

```sh
$ python3

Python 3.7.3  ...
```

Most contemporary Python software requires Python &ge; 3.7 at this time.
Let's install Bluez, which is a Bluetooth library:

```sh
sudo apt install bluez bluez-hcidump libbluetooth-dev

pip install --user pybluez
```

## Part 3: Wireless Sensor

(to be released September 9, 2021)
