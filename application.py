from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
import collector
import analyzer
import atexit

application = Flask(__name__)

@application.route("/")
def index():
    return "Follow @chain_well!"

def job():
    collector.verify_twitter_credentials()
    tweets = collector.get_tweets()
    #aggreagted_sentiment = analyzer.aggregate_sentiments(tweets)
    #print("Current twitter sentiment about BTC is: " + str(aggreagted_sentiment) + " out of 100")
    #print("Success")

scheduler = BackgroundScheduler()
scheduler.add_job(func=job, trigger="interval", seconds=60)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    application.run(port=5000, debug=True)
