import urllib2

def main():
	# open a connection to a URL using urllib2
	webURL = urllib2.urlopen("http://joemarini.com")

	# get the result code and print it
	print ("result code: " + str(webURL.getcode()))

	# read the data from the URL and print it
	data = webURL.read()
	print (data)

if __name__ == "__main__":
	main()