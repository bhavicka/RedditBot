import pylast
import re
import yaml
from lastfmapi import matchObj

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from http://www.last.fm/api/account for Last.fm
API_KEY = "2b8fbdd1799da50af34bc0cece4d3830" # this is a sample key
API_SECRET = "22fb38b141fb207f702299caf5c03700"

# In order to perform a write operation you need to authenticate yourself
username = "bhavicka"
password_hash = pylast.md5("bhavika1992")

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = 
    API_SECRET, username = username, password_hash = password_hash)

# now you can use that object every where
artist = network.get_artist("System of a Down")
# artist.shout("<3")

#time_periods = ['PERIOD_12MONTHS', 'PERIOD_6MONTHS', 'PERIOD_3MONTHS', 'PERIOD_OVERALL']
time_periods = ['PERIOD_6MONTHS']
top_tracks = []
#get top tracks for every time period
top_tracks = []
trackarray = []

#===============================================================================
# for time_period in time_periods:
# 	tracks = artist.get_top_tracks(3, time_period)
# 	print ("Data type",type(tracks));
# 
# for track in tracks:
# 	trackarray.append(str(track));
# 	yaml.load(track);
# 	print ("Appending new track array");
# 	
#===============================================================================
#===============================================================================
# for track in trackarray:
# 	print ("track", track);
# 	
# 	matchObj = re.match('.*[\s]-[\s](.*), Weight: [\d]+', track , re.M|re.I)
# 	#print ("group", matchObj.group(0)); #full Item object
# 	print ("group 2", matchObj.group(2)); #song name
#===============================================================================

artist = network.get_artist("Cher")

toptracks = artist.get_top_tracks(limit=3)

print type(toptracks)
      
for track in toptracks:
    for i in track:
        #print type(i)
        stringSong = str(i)
        
      

