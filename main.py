import requests
import time
from colorama import Fore, Style
import threading
import os
import random
import json
import base64

with open("config.json", encoding='utf-8', errors='ignore') as f:
  configdata = json.load(f, strict=False)
config = configdata["Config"]

tokenfile = config["tokenfile"]
proxyfile = config["proxyfile"]
tokens = open(tokenfile, 'r').read().splitlines()
proxies = open(proxyfile, 'r').read().splitlines()


def proxiesgen():
  return {"http": random.choice(proxies)}




for token in tokens:
  threading.Thread(target=Join, args=(token)).start()


headers2 = {
  "accept": "*/*",
  "authority": "discord.com",
  "method": "POST",
  "path": "/api/v9/auth/register",
  "scheme": "https",
  "origin": "discord.com",
  "referer": "discord.com/register",
  "x-debug-options": "bugReporterEnabled",
  "accept-language": "en-US,en;q=0.9",
  "connection": "keep-alive",
  "content-Type": "application/json",
  "user-agent":
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-origin",
}


def getcookie():
  r1 = requests.get("https://discord.com")
  cookie = r1.cookies.get_dict()
  cookie['locale'] = "us"
  return cookie


def getfingerprint():
  r2 = requests.get("https://discord.com/api/v9/experiments",
                    headers=headers2).json()
  fingerprint = r2["fingerprint"]
  return fingerprint

def dead(token):
  headers = {
    "authorization": token
  }
  if config["proxy"] == True:
    response = requests.post(f"https://discord.com/api/v6/invites/{random.choice(range(0,1000000))}",
                             headers=headers,,
                             proxies=proxiesgen())
    if response.status_code == 200:
      return
    else:
      if "captcha_key" in response.text:return
      else:
        print("[-] DeadToken : " + token)
  else:
    response = requests.post(f"https://discord.com/api/v6/invites/{random.choice(range(0,1000000))}",
                             headers=headers)
    if response.status_code == 200:
      return
    else:
      if "captcha_key" in response.text:return
      else:
        print("[-] DeadToken : " + token)
  Setup()
  Start()



def Join(token):
  properties = '{"os":"Windows","browser":"Chrome","device":"","system_locale":"ja","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36","browser_version":"103.0.0.0","os_version":"10","referrer":"","referring_domain":"","search_engine":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":139674,"client_event_source":null}'
  headers = {
    "authorization": token
  }
  if config["proxy"] == True:
    response = requests.post(f"https://discord.com/api/v6/invites/ctkp",
                             headers=headers,
                             cookies=getcookie(),
                             proxies=proxiesgen())
    if response.status_code == 200:
        while 1:threading.Thread(target=dead,args=(token,)).start()
    else:
      if "captcha_rqdata" and "captcha_key" in response.text:
        while 1:threading.Thread(target=dead,args=(token,)).start()
  else:
    response = requests.post(f"https://discord.com/api/v6/invites/ctkp",
                             headers=headers,
                             cookies=getcookie())
    if response.status_code == 200:
        while 1:threading.Thread(target=dead,args=(token,)).start()
    else:
      if "captcha_rqdata" and "captcha_key" in response.text:
        while 1:threading.Thread(target=dead,args=(token,)).start()
  Setup()
  Start()
