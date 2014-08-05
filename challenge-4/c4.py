import urllib2
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
id = '12345'
#id = '8022'

response = urllib2.urlopen(url + id)
text = response.read()
print text

while(True):

    response = urllib2.urlopen(url + id)
    text = response.read()

    print text

    new_id = "".join(re.findall(r'nothing is (\d*)', text))

    if new_id:
        print new_id
	id = new_id

    else:
	print "anwser = ", text
	break
