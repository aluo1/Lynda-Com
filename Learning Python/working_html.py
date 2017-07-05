# import the HTMLParser module
from HTMLParser import HTMLParser

metacount = 0

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	# this function will be called when the closing ">" of the tag is reached
	def handle_starttag(self, tag, attrs):
		global metacount

		print ("Encountered a start tag: {}".format(tag))
		if tag == "meta":
			metacount += 1

		pos = self.getpos() # return a tuple indication line and character
		print ("At line: {} position {}".format(pos[0], pos[1]))

		if attrs.__len__ > 0:
			print ("\tAttributes:")
			for a in attrs:
				print ("\t{} = {}".format(a[0], a[1]))

	# function to handle the ending tag
	def handle_endtag(self, tag):
		print ("Encountered an end tag: {}".format(tag))
		pos = self.getpos()
		print ("At line: {} position {}".format(pos[0], pos[1]))

	# function to handle the processing of HTML contents
	def handle_comment(self, data):
		print ("Encountered comment: {}".format(data))
		pos = self.getpos()
		print ("At line: {} position {}".format(pos[0], pos[1]))

def main():
	# instantiate the parser and feed it some HTML
	parser = MyHTMLParser()

	# open the sample HTML file and read it
	f = open("samplehtml.html")

	if f.mode == "r":
		contents = f.read() # read the entire file
		parser.feed(contents)

	print ("%d meta tags encountered" % metacount)

if __name__ == "__main__":
	main()