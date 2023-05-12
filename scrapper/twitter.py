import snscrape.modules.twitter as sntwitter


def get_only_tweets(username,count=50,since=2015):
    tweets=[]
    since = "{}-01-01".format(since)
    query = 'from:{} since:{}'.format(username,since)
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= count:
            break
        tweets.append(tweet.rawContent)
    return tweets

def get_detail_tweets(username,count=50,since=2015):
    tweets=[]
    since = "{}-01-01".format(since)
    query = 'from:{} since:{}'.format(username,since)
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= count:
            break
        tweets.append({"id":tweet.id,"date":tweet.date,"username":tweet.user.username, "content":tweet.rawContent})
    return tweets
