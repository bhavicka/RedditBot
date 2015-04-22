import praw
import pdb
import re
import os
import pylast
import getTopTracks
from config_bot import *
from config_lastfm import *
from getTopTracks import getArtist, getTopSongs



password_hash = pylast.md5(password)

#check whether a config file exists
if not os.path.isfile("config_bot.py"):
	print "Create a config file with your username and password first"
	exit(1)

if not os.path.isfile("config_lastfm.py"):
	print "Create a LAST.FM API Key file"
	exit(1)
	
#create an instance of our user agent

user_agent = ("lastfm toptracks 1.0")
r = praw.Reddit(user_agent = user_agent)


#login

r.login(REDDIT_USERNAME, REDDIT_PASS)


#save posts that we are replying to, each post has an id - a random string like 34hiojd
#first we assume that the file where we save these posts does not exist and create it

if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = [] 				#creates an empty list

else:
	with open("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read();
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = filter(None, posts_replied_to)


#now we get the top 5 hot posts from this subreddit

subreddit = r.get_subreddit('WhereDoIStart')

#lastfm access

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=SECRET_KEY, username=username, password_hash=password_hash)	

for submission in subreddit.get_hot(limit=7):
	
	#a post we have not replied to before
	if submission.id not in posts_replied_to:
		Posttitle = submission.title
		if Posttitle[:6] == '[META]':
			print "Skipped stickied post"		#skip this post
		else:
			artist = submission.title
			artist = artist[6:]
			print artist
			artistLastFm = getArtist(artist);
			print ("Last fm call for", artistLastFm)
		
			#use reg ex to check for a post title
			if re.search(artist, submission.title , re.IGNORECASE):		
				tracklist = getTopSongs(artistLastFm);
				for track in tracklist:
					for i in track:
						submission.add_comment("Top song by this artist: "+str(i))
						print "Bot replying to: " , submission.title
						posts_replied_to.append(submission.id)


#write our posts_replied_to list back to the file we created

with open("posts_replied_to.txt", "w") as f:
	for post_id in posts_replied_to:
		f.write(post_id +"\n")
