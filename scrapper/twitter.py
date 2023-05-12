import snscrape.modules.twitter as sntwitter


def get_only_tweets(username,count=50):
    tweets=[]
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:{}'.format(username)).get_items()):
        if i >= count:
            break
        tweets.append(tweet.rawContent)
    return tweets

def get_detail_tweets(username,count=50):
    tweets=[]
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:{}'.format(username)).get_items()):
        if i >= count:
            break
        tweets.append({"id":tweet.id,"date":tweet.date,"username":tweet.user.username, "content":tweet.rawContent})
    return tweets
