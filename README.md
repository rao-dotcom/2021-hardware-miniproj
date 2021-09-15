# 2021 Hardware Miniproject

Fall 2021 ECE Senior Capstone miniproject

[Report/Assignment](./Assignment.md)

First, [setup the Raspberry Pi hardware and operating system](./RaspberryPiSetup.md) Raspberry Pi OS.

Gain familiarity with Python and embedded sensors using the Raspberry Pi OS.
You can try the [Bluetooth](./bluetooth/) (suggest WiFi instead) and/or WiFi (suggested) examples [wifi_scan.py](./wifi_scan.py) in this project on the Raspberry Pi.

Finally, **collect and plot data using the Raspberry Pi as a wireless sensor**.

**NOTE**: There isn't so much easily scannable Bluetooth activity from automobiles. It's probably easiest to use WiFi example instead from the Senior Design lab or other room near a window facing the highway. WiFi range is up to about 20 meters, but can be longer.

Let's examine the possibility of detecting automobile, bicycle, and/or pedestrian activity in an area.
Many people carry smartphones or have automobiles that beacon wireless signals.
While more precise tracking requires multiple radio receivers, just using one receiver in our Raspberry Pi can give a sense of user activity in an area.

What would you like to measure via wireless activity in an area using a Raspberry Pi?
Ideas include:

* room occupancy trends
* traffic patterns (congestion of automobiles, bikes, and/or pedestrians)

Let discuss in class on Thursday, September 9, 2021 your ideas.
Each team could measure something a little different if they choose.

## General approach

The [wifi_scan.py](./wifi_scan.py)
example shows a way to log data to a JSON file over time, near the bottom of the Python script.
You'll find that some devices are always visible--they are probably fixed beacons, TVs, speakers, desktop computers, etc.
Devices like headphones, modern automobiles, etc. come and go as they move close to and away from the Raspberry Pi.

An issue with automobiles is not every modern automobile beacons BLE after its paired, or may only beacon during user setup interactions.
Let's use WiFi hotspots for detecting vehicles instead, and use [wifi_plot.py](./wifi_plot.py) to plot the data.

wifi_plot.py needs to be **run on your laptop**, as the Raspberry Pi has too old Python library versions to run the plots.
On your laptop, install the plotting packages like:

```sh
python3 -m pip install numpy xarray matplotlib
```

If you need to install Python itself, this is done like:

* Windows: via [Microsoft Store](https://www.microsoft.com/en-us/p/python-39/9p7qfqmjrfp7) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html#windows-installers)
* MacOS: via [Miniconda](https://docs.conda.io/en/latest/miniconda.html#macosx-installers)
* Linux: already installed on most Linux systems, or [Miniconda](https://docs.conda.io/en/latest/miniconda.html#linux-installers)

## WiFi hotspot detection in automobiles

Automobile hotspots have a specified range typically up to about 20 meters from the vehicle.
We are close enough to the road to be able to detect the vehicle WiFi hotspot as they travel past.
A typical WiFi beacon interval is 100 milliseconds.

The
[iw wireless toolkit](https://wireless.wiki.kernel.org/en/users/documentation/iw)
is available on many Linux systems including the Raspberry Pi OS.
We use this tool and parse its output in [wifi_scan.py](./wifi_scan.py) to detect WiFi hotspots, such as exist in modern automobiles.

```sh
sudo python3 wifi_scan.py ~/data -N 100
# logs data to ~/data and scans 100 times
```

copy this file to your laptop, perhaps using
[SCP](https://en.wikipedia.org/wiki/Secure_copy_protocol):

```sh
scp pi@raspberrypi.local:~/data/*.json .
```

---

Note, if you wish to measure/do something else with the Pi, please let us know and we'll discuss.
