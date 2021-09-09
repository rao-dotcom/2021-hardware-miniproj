"""
uses iwlist regex parsing from https://github.com/iancoleman/python-iwlist

iwlist is part of the Linux iw suite
"""

from __future__ import annotations
import pprint
import re
import subprocess
import argparse


cellRe = re.compile(r"^Cell\s+(?P<cellnumber>.+)\s+-\s+Address:\s(?P<mac>.+)$")
dataRe = [
    re.compile(r"^ESSID:\"(?P<essid>.*)\"$"),
    re.compile(
        r"^Frequency:(?P<frequency>[\d.]+) (?P<frequency_units>.+) \(Channel (?P<channel>\d+)\)$"
    ),
    re.compile(
        r"^Quality=(?P<signal_quality>\d+)/(?P<signal_total>\d+)\s+Signal level=(?P<signal_level_dBm>.+) d.+$"
    ),
    re.compile(r"^Signal level=(?P<signal_quality>\d+)/(?P<signal_total>\d+).*$"),
]


def scan(iface: str) -> str:
    """
    use command line to scan for Wifi networks
    """
    cmd = ["iwlist", iface, "scan"]
    return subprocess.check_output(cmd, text=True)


def parse(raw: str) -> dict[str, dict[str, str]]:
    """
    parse iwlist scan output
    """

    aps: dict[str, dict[str, str]] = {}
    for line in raw.split("\n"):
        line = line.strip()

        cell = cellRe.search(line)
        if cell:
            bssid = cell.group(2)
            aps[bssid] = {}
            continue

        for dat in dataRe:
            r = dat.search(line)
            if r:
                aps[bssid].update(r.groupdict())

    return aps


if __name__ == "__main__":
    P = argparse.ArgumentParser(description="WiFi scanner using iw")
    P.add_argument("-i", "--interface", default="wlan0", help="WiFi interface to scan")
    args = P.parse_args()

    raw = scan(iface=args.interface)
    # raw = open("input.txt").read()

    aps = parse(raw)
    pprint.pprint(aps)
