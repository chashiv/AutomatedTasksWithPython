# Author : Shivam Chauhan
# Date   : March 6, 2019

# This scripts takes search matter as input and open up the best 
# matched links(on the first page usually) in new tabs in the browser
# automatically.

from bs4 import BeautifulSoup
import requests
import webbrowser

content = input("Enter the content to be searched : ") # Get the content
urlAddress = 'http://google.com/search?q=' + content  # Set up Url
try:
	res = requests.get(urlAddress) # Get request object
	res.raise_for_status() # Check the status
	webbrowser.open(urlAddress) # Open browser's windows
	soup = BeautifulSoup(res.text, 'html.parser')
	linkElements = soup.select('.r a')
	numOpen = min(5, len(linkElements))
	for i in range(numOpen): # Opening up of tabs
		webbrowser.open('http://google.com' + linkElements[i].get('href'))
except Exception as err:
	print("Oops!!, you entered a wrong URL " )