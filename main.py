"""
****************************************************************************
𝕻𝖗𝖔𝖌𝖗𝖆𝖒 𝕹𝖆𝖒𝖊 : 𝖂𝖎𝖋𝖎 𝕻𝖆𝖘𝖘𝖜𝖔𝖗𝖉 𝕰𝖝𝖙𝖗𝖆𝖈𝖙𝖔𝖗
𝕬𝖚𝖙𝖍𝖔𝖗        : 𝕸𝖔𝖓𝖙𝖆𝖘𝖎𝖒
𝕮𝖗𝖊𝖆𝖙𝖊𝖉 𝖔𝖓     : 10.11.2020
𝕮𝖔𝖓𝖙𝖆𝖈𝖙        : 𝖍𝖙𝖙𝖕𝖘://𝖌𝖎𝖙𝖍𝖚𝖇.𝖈𝖔𝖒/𝖒𝖔𝖓𝖙𝖆𝖘𝖎𝖒

# used variables in this program
----------------------------------------------------------------------------
data    - get output when first command is executed
wifis   - get all wifi name from user machine
results - get wifi passwords
*****************************************************************************
"""

#   for executing terminal command through python
import subprocess

#   decode output because it will get encoded output
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
#   get all wifi network name
wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]
#   shows output data
#   print(data)
#   shows all wifi name
#   print(wifis)

#   get wifi password
for wifi in wifis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split(
        '\n')
    results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
    try:
        print(f'Name : {wifi}, Password : {results[0]}')
        #   saving subdomains in a file
        # file = open('wifi password.txt', "a", encoding="utf8")
        # file.write(f'Name : {wifi}, Password : {results[0]}' + '\n')
    except IndexError:
        print(f'Name : {wifi}, Password : Not found!')

"""
────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──────────██████─██████████████─████████████───██████████████────██████████████───████████──████████─
─██░░██████████████░░██─██░░░░░░░░░░██─██░░░░░░░░████─██░░░░░░░░░░██────██░░░░░░░░░░██───██░░░░██──██░░░░██─
─██░░░░░░░░░░░░░░░░░░██─██░░██████░░██─██░░████░░░░██─██░░██████████────██░░██████░░██───████░░██──██░░████─
─██░░██████░░██████░░██─██░░██──██░░██─██░░██──██░░██─██░░██────────────██░░██──██░░██─────██░░░░██░░░░██───
─██░░██──██░░██──██░░██─██░░██████░░██─██░░██──██░░██─██░░██████████────██░░██████░░████───████░░░░░░████───
─██░░██──██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██────██░░░░░░░░░░░░██─────████░░████─────
─██░░██──██████──██░░██─██░░██████░░██─██░░██──██░░██─██░░██████████────██░░████████░░██───────██░░██───────
─██░░██──────────██░░██─██░░██──██░░██─██░░██──██░░██─██░░██────────────██░░██────██░░██───────██░░██───────
─██░░██──────────██░░██─██░░██──██░░██─██░░████░░░░██─██░░██████████────██░░████████░░██───────██░░██───────
─██░░██──────────██░░██─██░░██──██░░██─██░░░░░░░░████─██░░░░░░░░░░██────██░░░░░░░░░░░░██───────██░░██───────
─██████──────────██████─██████──██████─████████████───██████████████────████████████████───────██████───────
────────────────────────────────────────────────────────────────────────────────────────────────────────────
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──────────██████─██████████████─██████──────────██████─██████████████─██████████████─██████████████─██████████─██████──────────██████─
─██░░██████████████░░██─██░░░░░░░░░░██─██░░██████████──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░██─██░░██████████████░░██─
─██░░░░░░░░░░░░░░░░░░██─██░░██████░░██─██░░░░░░░░░░██──██░░██─██████░░██████─██░░██████░░██─██░░██████████─████░░████─██░░░░░░░░░░░░░░░░░░██─
─██░░██████░░██████░░██─██░░██──██░░██─██░░██████░░██──██░░██─────██░░██─────██░░██──██░░██─██░░██───────────██░░██───██░░██████░░██████░░██─
─██░░██──██░░██──██░░██─██░░██──██░░██─██░░██──██░░██──██░░██─────██░░██─────██░░██████░░██─██░░██████████───██░░██───██░░██──██░░██──██░░██─
─██░░██──██░░██──██░░██─██░░██──██░░██─██░░██──██░░██──██░░██─────██░░██─────██░░░░░░░░░░██─██░░░░░░░░░░██───██░░██───██░░██──██░░██──██░░██─
─██░░██──██████──██░░██─██░░██──██░░██─██░░██──██░░██──██░░██─────██░░██─────██░░██████░░██─██████████░░██───██░░██───██░░██──██████──██░░██─
─██░░██──────────██░░██─██░░██──██░░██─██░░██──██░░██████░░██─────██░░██─────██░░██──██░░██─────────██░░██───██░░██───██░░██──────────██░░██─
─██░░██──────────██░░██─██░░██████░░██─██░░██──██░░░░░░░░░░██─────██░░██─────██░░██──██░░██─██████████░░██─████░░████─██░░██──────────██░░██─
─██░░██──────────██░░██─██░░░░░░░░░░██─██░░██──██████████░░██─────██░░██─────██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░██─██░░██──────────██░░██─
─██████──────────██████─██████████████─██████──────────██████─────██████─────██████──██████─██████████████─██████████─██████──────────██████─
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
"""
