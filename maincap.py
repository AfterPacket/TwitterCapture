import tweepy
from PIL import Image

# Replace these with your own Twitter API keys
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# The Twitter user whose tweets you want to capture
user = 'YOUR_TWITTER_USER_HERE'

# Get the user's tweets
tweets = api.user_timeline(screen_name=user, count=100)

# For each tweet, save a screenshot of it to a file
for tweet in tweets:
    img = Image.open(tweet.text)
    img.save(tweet.id_str + '.png')

# Print out the user names of the users who tweeted the tweets
for tweet in tweets:
    print(tweet.user.screen_name)
