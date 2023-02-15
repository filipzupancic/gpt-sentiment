import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_KEY_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(
  consumer_key, 
  consumer_secret, 
  access_token, 
  access_token_secret
)

api = tweepy.API(auth)
#stream = tweepy.Stream(auth)

class MyStream(tweepy.Stream):
    def on_status(self, status):
        print(status.id)
        print(status.text)

def verify_twitter_credentials():
    try:
        api.verify_credentials()
        print("Authentication Successful")
    except:
        print("Authentication Error")

def get_tweets():
    myStream = MyStream(consumer_key, consumer_secret, access_token, access_token_secret)
    myStream.filter(track=["Bitcoin"])
    myStream.sample()
    #return api.search_tweets("tesla from:elonmusk lang:en -is:retweet", tweet_mode="extended", count=5)

if __name__ == "__main__":
    get_tweets()
    