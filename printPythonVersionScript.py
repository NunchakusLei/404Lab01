#!/usr/bin/env python

import requests

print requests.__version__

response = requests.get("https://raw.githubusercontent.com/NunchakusLei/404Lab01/master/printPythonVersionScript.py")
print response.text
print response.status_code
