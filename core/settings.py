#!/usr/bin/env python

"""
Copyright (c) 2015 Miroslav Stampar (@stamparm)
See the file 'LICENSE' for copying permission
"""

import os
import socket
import stat
import subprocess

CAPTURE_FILTER = "(tcp[13] == 2) or not tcp"  # SYN or not TCP
MONITOR_INTERFACE = "any"
SNAP_LEN = 100
IPPROTO = 8
ETH_LENGTH = 14
WRITE_PERIOD = 60 * 15
IPPROTO_LUT = dict(((getattr(socket, _), _.replace("IPPROTO_", "")) for _ in dir(socket) if _.startswith("IPPROTO_")))
LOCAL_ADDRESSES = []
BLACKLISTED_ADDRESSES = ("255.255.255.255", "127.0.0.1", "0.0.0.0")
DATE_FORMAT = "%Y-%m-%d"
SYSTEM_LOG_DIRECTORY = "/var/log" if not subprocess.mswindows else "C:\\Windows\\Logs"
LOG_DIRECTORY = os.path.join(SYSTEM_LOG_DIRECTORY, "tsusen")
DEFAULT_LOG_PERMISSIONS = stat.S_IREAD | stat.S_IWRITE | stat.S_IRGRP | stat.S_IROTH
CSV_HEADER = "proto dst_port dst_ip src_ip first_seen last_seen count"