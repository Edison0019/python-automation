#this program is for launching addresses to the google map web app
#from the command line or from the clipboard


import sys, webbrowser,pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)