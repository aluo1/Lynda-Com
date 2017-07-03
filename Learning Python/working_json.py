import urllib2
import json

def printResults(data):
	# use the JSON module to load the string data into dictionary
	theJSON = json.loads(data)

	# now we can access the contents of JSON like any other Python objects
	if "title" in theJSON["metadata"]:
		print (theJSON["metadata"]["title"])

	# output the numver of events, plus the magnitude and each event name
	count = theJSON["metadata"]["count"]
	print (str(count) + " events recorded")

	# for each event, print the place where it occurred
	for i in theJSON["features"]:
		print i["properties"]["place"]

	# print the events that only have a magnitude greater than 4
	for i in theJSON["features"]:
		if i["properties"]["mag"] >= 4.0:
			print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"])

	# print only the events where at least 1 person reported feeling something
	print ("Events that are felt: ")
	for i in theJSON["features"]:
		feltReports = i["properties"]["felt"]

		if (feltReports != None) and (feltReports > 0):
			print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported {} times".format(str(feltReports)))



def main():
	urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

	# open the URL and read the data
	webURL = urllib2.urlopen(urlData)
	webCode = webURL.getcode()
	print (webCode)

	if (webCode == 200):
		data = webURL.read()
		
		# print out the customized results
		printResults(data)
	else:
		print ("Received an error from server, cannot retrieve results " + str(webCode))


if __name__ == "__main__":
	main()