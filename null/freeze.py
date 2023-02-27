from py2exe import freeze


import binascii
import defaults
import multiprocessing 
import os
import platform
import sys
import time
import unicodedata
import xml.etree.cElementTree 



freeze(
options = {'py2exe': {'bundle_files': 1, 'compressed': True,}},
console=['main.py'],
zipfile = None,

)