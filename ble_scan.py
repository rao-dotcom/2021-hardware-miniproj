#!/usr/bin/env python3
"""
Example of scanning Bluetooth Low Energy (BLE) devices
"""

from bluetooth.ble import DiscoveryService

TIMEOUT = 10  # arbitrary, seconds

svc = DiscoveryService()
ble_devs = svc.discover(TIMEOUT)

for u, n in ble_devs.items():
    print(u, n)
