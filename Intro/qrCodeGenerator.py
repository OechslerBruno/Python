# -*- coding: utf-8 -*-
"""
pip install pyqrcode
pip install pypng

@author: Bruno
"""

import pyqrcode
import png
from pyqrcode import QRCode

urlString = "https://www.google.com/"

url = pyqrcode.create(urlString)
url.png("C:\\Users\\Bruno\\Desktop\\qr.png", scale=8)