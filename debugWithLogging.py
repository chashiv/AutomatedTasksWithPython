# Author : Shivam Chauhan
# Date   : March 6, 2019

# This is a simple demonstration to use/implement debugging with
# logging module

'''
	2019-04-06 22:19:11,484 - DEBUG - Came Inside Function
	2019-04-06 22:19:11,484 - DEBUG - i : 1 total : 1
	2019-04-06 22:19:11,484 - DEBUG - i : 2 total : 2
	2019-04-06 22:19:11,484 - DEBUG - i : 3 total : 6
	2019-04-06 22:19:11,484 - DEBUG - i : 4 total : 24
	2019-04-06 22:19:11,484 - DEBUG - i : 5 total : 120
	2019-04-06 22:19:11,484 - DEBUG - END
	120
'''


import logging

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

def fact(n):
	'''
		Returns the factorial of the number n
	'''
	logging.debug("Came Inside Function")
	total = 1
	for i in range(1, n+1):
		total *= i
		logging.debug("i : "+ str(i) + " total : " + str(total))
	logging.debug("END")
	return total

# logging.disable(logging.CRITICAL) # Can be used to disable the log messages
print(fact(5))
