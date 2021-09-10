# Bluetooth on Raspberry Pi / Linux

The PyBluez package requires a Linux computer such as the Raspberry Pi for full functionality including BLE.

```sh
sudo apt install bluez bluez-hcidump libbluetooth-dev libglib2.0-dev libboost-python-dev libboost-thread-dev
# drivers needed by PyBluez

sudo python3 -m pip install pybluez gattlib
```

Normally we avoid using "sudo" to install Python packages, but in this case we will also need to run Python with "sudo" to access hardware.
We use "python3 -m pip" to avoid installing the deprecated Python 2 package.

Let's check if the Bluetooth hardware is enabled.
Let's reboot the Pi to ensure the driver updates are enabled:

```sh
sudo reboot
```

List the Bluetooth devices:

```sh
$ sudo bluetoothctl list

Controller <hex-address> raspberrypi [default]
```

If nothing is listed, the Bluetooth hardware is not enabled.
Try rebooting the Pi if this occurs.
Also check that Bluetooth isn't blocked:

```sh
$ rfkill list all

0: phy0: Wireless LAN
        Soft blocked: no
        Hard blocked: no
1: hci0: Bluetooth
        Soft blocked: no
        Hard blocked: no
```

See what BLE devices are wirelessly visible near the Pi:

```sh
$ $ sudo bluetoothctl scan on
Discovery started
[CHG] Controller DC:A6:32:65:2B:47 Discovering: yes
# ongoing stream of devices heard, should take only a few seconds to start seeing devices
# if any Bluetooth devices are advertising nearby (within about 100 meters).
```

---

The example [ble_scan.py](./ble_scan.py) Python script is run with "sudo" to access hardware like:

```sh
python3 ble_scan.py
```

The script can be enhanced to log data to disk or the cloud, capturing Bluetooth activity vs. time to estimate human activity in a vicinity with the Raspberry Pi sitting somewhere.
