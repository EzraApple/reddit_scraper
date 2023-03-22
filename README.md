# reddit_scraper
A simple command line scraper to get subreddit top post information using several sorting methods.
In order to use this program, you must input some personal information
so that it works through your account/app

For the variables named "username" and "password", put your reddit username and password

For the variables named "appKey" and "secretKey", go to 'https://www.reddit.com/prefs/apps/' 
and create an app (script for personal use). Input the app key into "appKey" and the secret 
into "secretKey"

With the empty variables filled with this information, you will be able to access the reddit API 
and get information about posts in subreddits (title and user).

When the script is run from the command line, you will be prompted for subreddit, sorting method,
possibly timeframe, and number of posts.
