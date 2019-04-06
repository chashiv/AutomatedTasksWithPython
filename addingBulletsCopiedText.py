# Author : Shivam Chauhan
# Date   : March 6, 2019

# This programs adds bullets(wiki) to the copied text on clipboard and
# copies back the formatted text to the clipboard again


import pyperclip
text = pyperclip.paste() # Store copied code from clipboard
lines = text.split("\n") 
for index in range(len(lines)):
	lines[index] = "* " + lines[index].strip()
text = "\n".join(lines)
pyperclip.copy(text)