import urllib2

#For pictures
#import urllib
#urllib.urlretrieve("<URL>", 
#					"<FILE NAME>.<EXT>")

def downloadfile(download_url):
    response = urllib2.urlopen(download_url)
    file = open("download.pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Done")

def run():
	url = ""
	id = 0
	while id < 10000000:
		try:
			downloadfile(url + str(id))
			return
		except:
			print id
			id+=1

run()