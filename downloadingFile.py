# Author : Shivam Chauhan
# Date   : March 6, 2019

# This scripts take url of remote file as an input if it exits, it will
# download the contents of the file in the current working directory
# to the file named as "backup.txt" else it will report an error

import requests
urlAddress = input("Enter the URL : ") # Get the URL
res = requests.get(urlAddress)
try:
	res.raise_for_status() # Check for the status
	# Open/Create the file, write in binary mode
	backupFile = open("backup.txt", 'wb') 
	for chunks in res.iter_content(len(res.text)):
		backupFile.write(chunks)
	backupFile.close() # Close the file
except Exception as err:
	print("Oops!! " + str(err))
