# RedditBot

This is a Reddit bot to submit the top track of an artist from Last.fm data to a comment in r/WhereDoIStart

I use the subreddit called WhereDoIStart because it's for helping people get into artists with huge discographies.
The submission title gets me the artist name which I use to extract the Top Track from Last.fm.
I'm using Pylast (https://github.com/pylast/pylast) which is a Python wrapper for the Last.fm API.

Try it out by running the reply_post.py script.

You can automate this script by setting up a cron job (Linux) or using Task Scheduler (Windows). 

