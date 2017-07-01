import os
from os import path
from datetime import date, time, timedelta, datetime
import time

def main():
	file_name = "working_calendar.py"

	print ("Print the OS name")
	# print the name of os
	print (os.name)

	print ("\nCheck the file working_calendar.py existence and type")
	# check for item existence and type
	print ("Item exists: " + str(path.exists(file_name)))
	print ("Item is a file: " + str(path.isfile(file_name)))
	print ("Item is a directory: " + str(path.isdir(file_name)))

	print ("\nPrint file path")
	# work with file path
	print ("Item path: " + str(path.realpath(file_name)))
	print ("Item path and name: " + str(path.split(path.realpath(file_name))))

	print ("\nPrint file modification time")
	# get modification time
	t = time.ctime(path.getmtime(file_name))
	print (t)
	print (datetime.fromtimestamp(path.getmtime(file_name)))

	print ("\nCalculate how long ago the time was modified")
	# calculate how long ago the time was modified
	td = datetime.now() - datetime.fromtimestamp(path.getmtime(file_name))
	print ("It has been " + str(td) + " this file was modified")
	print ("Or, " + str(td.total_seconds()) + " seconds.")


if __name__ == "__main__":
	main()