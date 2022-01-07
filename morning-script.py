#!/usr/bin/env python

# based on Lucas Soares' code
import webbrowser
import time
import os
import subprocess
from datetime import datetime
import json
import sys
import urllib.request


def sendNotificationOnLinux(message):
    subprocess.Popen(['notify-send', '--hint=int:transient:1', message])
    return


def continueDay():
    cont = input("Press to continue")


# Print currency
url = 'https://api.exchangerate-api.com/v4/latest/USD'
f = urllib.request.urlopen(url)
obj = json.loads(f.read())
sendNotificationOnLinux(
    "1 USD is " + "{:,.2f}".format(obj['rates']['CAD']) + " CAD today")


# Google calendar events
sendNotificationOnLinux("Check your calendar")
webbrowser.open("https://calendar.google.com/calendar/u/0/r/day")

# teams, mail, slack, whatsapp
sendNotificationOnLinux("Check my tasks")
os.system("todoist")
continueDay()


# Google calendar events
sendNotificationOnLinux("Read papers")
webbrowser.open("https://feedly.com")
continueDay()


# Google calendar events
sendNotificationOnLinux("Read Python chapter")
continueDay()


sendNotificationOnLinux("Check emails")
webbrowser.open("https://www.messenger.com")
webbrowser.open("https://web.whatsapp.com/")
webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
continueDay()
