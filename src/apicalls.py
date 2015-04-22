import json
import urllib2
from xml.dom import minidom
import pylast
import lastfmapitrial

artist = "Cher";

link = "http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist="+artist+"&limit=3&api_key=2b8fbdd1799da50af34bc0cece4d3830&format=json"

linkxml = "http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist="+artist+"r&limit=3&api_key=2b8fbdd1799da50af34bc0cece4d3830"

data = urllib2.urlopen(linkxml)

print type(data)

xmldoc = minidom.parse(data)

for element in xmldoc.getElementsByTagName('toptracks'):
    print element

print "Finished"

