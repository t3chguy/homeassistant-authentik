#!/usr/bin/env python
import os
import sys
import requests
from http.cookiejar import CookieJar

AUTHENTIK_URL = "https://auth.server.tld"
AUTHENTIK_FLOW = "password-authentication-flow"

URL = f"{AUTHENTIK_URL}/api/v3/flows/executor/{AUTHENTIK_FLOW}/"

jar = CookieJar()
req = requests.get(URL, cookies=jar)
component = req.json()["component"]

data = dict(component=component, uid_field=os.environ.get("username"), password=os.environ.get("password"))
req = requests.post(URL, cookies=jar, json=data)
component = req.json()["component"]

if component != "xak-flow-redirect":
    sys.exit(1)
