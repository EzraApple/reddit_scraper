# Goal: Access reddit API to get desired info.
# User inputs subreddit name, a number of posts,
# how to sort, etc. Program will return itemized list of titles and such
# -Ezra Apple
import requests
from requests.auth import HTTPBasicAuth

# your reddit account details
username = ''  # reddit username
password = ''  # reddit password

# your app id / secret
appKey = ""
secretKey = ""

# get authorization using app id/secret
auth = requests.auth.HTTPBasicAuth(appKey, secretKey)

# dict for storing account details
data = {
    'grant_type': 'password',
    'username': username,
    'password': password
}

# headers
headers = {
    "User-Agent": "subScraper01"
}

# get auth token for account and app details
results = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
auth_token = results.json()['access_token']

# add token to headers
headers['Authorization'] = f'bearer {auth_token}'

# get user input on what they want
subreddit = input("Enter a subreddit name: ")
sortBy = input("How to sort? (top, hot, new, controversial): ").lower()
timeframe = ""
if sortBy.__eq__("top") or sortBy.__eq__("controversial"):
    timeframe = "t=" + input("Time frame of sort? (hour, day, week, month, year, all): ") + "&"
limit = "limit=" + input("How many posts? (1-50): ")

# assemble requests url and get data
url = f'https://oauth.reddit.com/r/{subreddit}/{sortBy}' + "?" + timeframe + limit
results = requests.get(url, headers=headers)

# loop through json and print out posts and users
count = 1
print("\n")
for post in results.json()['data']['children']:
    title = post['data']['title']
    user = post['data']['author']
    print(f'{count}. "{title}" by u/{user}')
    count += 1

# give link to reddit page
print(f"\nLink: https://www.reddit.com/r/{subreddit}/{sortBy}""?" + timeframe + limit)