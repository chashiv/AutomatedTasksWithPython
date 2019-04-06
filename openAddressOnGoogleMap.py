# Author : Shivam Chauhan
# Date   : March 6, 2019

# This programs takes address as command line argument and then points
# the location on the google map in the browser window
# either provide address as command line argument or just copy the
# address before running this script 

import pyperclip
import sys
import webbrowser

if len(sys.argv) > 1:
	# Get arguments 
	address = " ".join(sys.argv[1:])
else:
	# Get the copied text 
	address = pyperclip.paste()

urlAddress = 'https://google.com/maps/place/' + address 
webbrowser.open(urlAddress) # Open the browser window with respective url
