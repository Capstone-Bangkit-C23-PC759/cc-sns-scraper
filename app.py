import json
from flask import Flask
import snscrape.modules.twitter as sntwitter

app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello_word():
    return "<h1>Hello Word</h1>"

@app.route("/tweets",methods=['GET'])
def get_tweets():
    tweets = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:ainurohman').get_items()):
        if i > 5:
            break
        tweets.append(tweet.rawContent)
        
    return json.dumps(tweets,default=str)