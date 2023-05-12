import json
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
    if type(username) != str or len(username) < 3 :
        return json.dumps({"code":400,"message":"missing param /username/ or value to short. min length is 3 char "}), 400
    if type(count) == str:
        try:
            count = int(count)
            if count > 100 or count  < 1:
                return json.dumps({"code":400,"message":"param /count/  max length is 100 and min length is 1."}), 400
        except:
            return json.dumps({"code":400,"message":"param /count/ should be integer."}), 400
    else:
        count = 50
    tweets = twitter.get_only_tweets(username,count)
    return json.dumps(tweets)

@app.route("/twitter/tweets/detail",methods=['GET'])
def get_tweets_detail():
    username = request.args.get('username')
    count = request.args.get('count')
    if type(username) != str or len(username) < 3 :
        return json.dumps({"code":400,"message":"missing param /username/ or value to short. min length is 3 char "}), 400
    if type(count) == str:
        try:
            count = int(count)
            if count > 100 or count  < 1:
                return json.dumps({"code":400,"message":"param /count/  max length is 100 and min length is 1."}), 400
        except:
            return json.dumps({"code":400,"message":"param /count/ should be integer."}), 400
    else:
        count = 50
    tweets = twitter.get_detail_tweets(username,count)
    return json.dumps(tweets,default=str)