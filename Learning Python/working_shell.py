import os
import shutil
from os import path
from datetime import datetime
from zipfile import ZipFile

def main():
	file_name = "working_os.py"

	print ("Duplicate existing file")
	# make a duplicate of existing file.
	if path.exists(file_name):
		# get the path to the file in the current directory
		src = path.realpath(file_name)

		# seperate the path part from the file name
		head, tail = path.split(src)
		print ("head: " + head)
		print ("tail: " + tail)

		# let's make a backup copy by appending 'bak' to the name
		dst = src + ".bak"
		# now use the shell utility to make a copy of the file
		shutil.copy(src, dst)
		print ("Modification time for file copied using .copy(): " + str(datetime.fromtimestamp(path.getmtime(dst))))

		# copy over the permissions, modification times and other info
		shutil.copystat(src, dst)		
		print ("Modification time for file copied using .copystat(): " + str(datetime.fromtimestamp(path.getmtime(dst))))

		print ("\nRename the backup file")
		# rename of backup file
		os.rename(dst, dst + ".stat")

		print ("\nPut the backup file into a ZIP archive ")
		# now put things into a ZIP archive
		root_dir, tail = path.split(path.realpath(dst))
		shutil.make_archive("archive", "zip", root_dir)

		print ("\nDo more fine-grained control over ZIP files")
		# more fine-grained control over ZIP files
		with ZipFile("testzip.zip", "w") as newzip:
			newzip.write("working_os.py.bak.stat")
			newzip.write("working_calendar.py")


if __name__ == "__main__":
	main()