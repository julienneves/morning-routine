#!/usr/bin/env python

# based on Lucas Soares' code
import webbrowser
import os
import subprocess
from datetime import datetime, timedelta
import json
import csv
import urllib.request


def sendNotificationOnLinux(message):
    subprocess.Popen(['notify-send', '--hint=int:transient:1', message])
    return


def continueDay():
    cont = input("Press to continue")


def boolInput(prompt):
    answer = input(prompt)
    if answer.lower().startswith("y"):
        cond = True
    elif answer.lower().startswith("n"):
        cond = False
    else:
        cond = ""
    return(cond)


answer = input("Do I want to run my morning routine script? (y/n)")
if answer.lower().startswith("n"):
    exit()
elif answer.lower().startswith("y"):
    # Resolution
    print("New Year's resolutions tally")

    yesterday = datetime.now().date() - timedelta(days=1)
    resolution_row = [yesterday]

    if yesterday.month == 1:
        resolution_row.append(boolInput("Found a new idea? (y/n)"))
    elif yesterday.month == 2:
        resolution_row.append(
            boolInput("Completed analysis on for JMP? (y/n)"))
    else:
        resolution_row.append(boolInput("Wrote a first draft? (y/n)"))

    resolution_row.append(boolInput("Read a paper? (y/n)"))
    resolution_row.append(boolInput("Meditated for 15 minutes? (y/n)"))
    resolution_row.append(boolInput("Trained for more than 30 minutes? (y/n)"))
    resolution_row.append(boolInput("Didn't drink an energy drink? (y/n)"))
    resolution_row.append(boolInput("Drank 3 bottles of water? (y/n)"))
    resolution_row.append(boolInput("Didn't bite my nails? (y/n)"))

    resolution_row
    with open('/home/julien/Dropbox/Miscellaneous/new-year-resolution.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(resolution_row)

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
    sendNotificationOnLinux("Read abstracts of new working papers")
    webbrowser.open("https://feedly.com")
    continueDay()

    # Google calendar events
    sendNotificationOnLinux("Read a paper")
    continueDay()

    sendNotificationOnLinux("Check emails")
    webbrowser.open("https://www.messenger.com")
    webbrowser.open("https://web.whatsapp.com/")
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
    continueDay()

    print("Start this motherfucking day")
