import json
import datetime
from flask import Flask
from flask import request
from scrapper import twitter

app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello_word():
    return "<h1>Hello Word</h1>"

@app.route("/twitter/tweets",methods=['GET'])
def get_tweets():
    username = request.args.get('username')
    count = request.args.get('count')
    since = request.args.get('since')
    if type(username) != str or len(username) < 3 :
        return json.dumps({"code":400,"message":"missing param /username/ or value to short. min length is 3 char "}), 400

    if type(count) == str:
        try:
            count = int(count)
            if count > 1000 or count  < 1:
                return json.dumps({"code":400,"message":"param /count/  max length is 100 and min length is 1."}), 400
        except:
            return json.dumps({"code":400,"message":"param /count/ should be integer."}), 400
    else:
        count = 50
    if type(since) == str:
        year_today = int(datetime.date.today().year)
        try:
            since = int(since)
            if   since > year_today   or since  <  2015:
                return json.dumps({"code":400,"message":"param /since/  max  value is {} and min value is 2015.".format(year_today)}), 400
        except:
            return json.dumps({"code":400,"message":"param /since/ should be integer."}), 400
    else:
        since = 2015

    tweets = twitter.get_only_tweets(username,count,since)
    return json.dumps(tweets)

@app.route("/twitter/tweets/detail",methods=['GET'])
def get_tweets_detail():
    username = request.args.get('username')
    count = request.args.get('count')
    since = request.args.get('since')
    if type(username) != str or len(username) < 3 :
        return json.dumps({"code":400,"message":"missing param /username/ or value to short. min length is 3 char "}), 400

    if type(count) == str:
        try:
            count = int(count)
            if count > 1000 or count  < 1:
                return json.dumps({"code":400,"message":"param /count/  max length is 100 and min length is 1."}), 400
        except:
            return json.dumps({"code":400,"message":"param /count/ should be integer."}), 400
    else:
        count = 50

    if type(since) == str:
        year_today = int(datetime.date.today().year)
        try:
            since = int(since)
            if   since > year_today   or since  <  2015:
                return json.dumps({"code":400,"message":"param /since/  max  value is {} and min value is 2015.".format(year_today)}), 400
        except:
            return json.dumps({"code":400,"message":"param /since/ should be integer."}), 400
    else:
        since = 2015

    tweets = twitter.get_detail_tweets(username,count,since)
    return json.dumps(tweets,default=str)