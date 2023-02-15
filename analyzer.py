import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def determine_tweet_sentiment(tweet):
    response_sentiment = openai.Completion.create(
        model="text-davinci-003",
        prompt="Rate tweet sentiment on a scale from 1 to 100 only with a number.\n\nTweet: " + tweet + " Sentiment:",
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    return int(response_sentiment["choices"][0]["text"])

def aggregate_sentiments(tweets):
    number_of_tweets = len(tweets)
    aggregated_sentiment = 0
    for tweet in tweets:
        sentiment = 50 # neutral
        print(tweet.author.screen_name)
        print(tweet.id)
        try:
            #print(tweet.retweeted_status.full_text)
            sentiment = determine_tweet_sentiment(tweet.retweeted_status.full_text)
            #print(sentiment)
            aggregated_sentiment += sentiment
            #print("=====")
        except AttributeError:
            #print(tweet.full_text)
            sentiment = determine_tweet_sentiment(tweet.full_text)
            #print(sentiment)
            aggregated_sentiment += sentiment
            #print("=====")
    return aggregated_sentiment / number_of_tweets

#api.update_status("I'm much more confident with crypto than with banks or fiat currency because I can actually control it, and the money supply is transparent, stated up front. It makes online shopping a lot easier and a lot safer.")
    