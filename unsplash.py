import requests
import json
import urllib
import os 

#Authorization: Client-ID b368f491e16ba073bcbccc2a10fe94153cb01377e9e7dad6ffca0ec9f19400fe

x = raw_input("What type of picture do you want? ")
y = raw_input("Number of pictures? ")
my_url = "https://api.unsplash.com/photos/search?client_id=b368f491e16ba073bcbccc2a10fe94153cb01377e9e7dad6ffca0ec9f19400fe"
add = "&query=" + str(x) + "&per_page=" + str(y) 
my_url+=add 

htmlfile = requests.get(my_url)
parsed_json = json.loads(htmlfile.text)

#print parsed_json
i = 0
dire = str(x)

if os.path.exists(dire):
	os.chdir(dire)
else:
    os.makedirs(dire)
    os.chdir(dire)
'''
def makemydir(dire):
  try:
    os.makedir(dire)
  except OSError:
    pass
  # let exception propagate if we just can't
  # cd into the specified directory
  os.chdir(dire)
 '''
'''
def getpics(dire, exits):
	if exists:
		i
		'''

while i < len(parsed_json):
	print json.dumps(parsed_json[i]["links"]["download"], sort_keys=True, indent=4)
	urllib.urlretrieve(parsed_json[i]["links"]["download"] , dire + str (i+1) + ".jpg")
	i += 1

#urllib.urlretrieve(parsed_json["links"]["download"] , "3.jpg") 
#urllib.urlretrieve(parsed_json["urls"]["full"] , "1.jpg")
	