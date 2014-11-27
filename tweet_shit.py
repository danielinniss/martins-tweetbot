import tweepy
import random_lines

consumer_key = 'x1ncxKWAK93HDjOCqDW9iWoIw'
consumer_secret = 'r14HdhJhZpXMehGtcPooAFt8MD5Da9BSgQWnoYYlL1UPUq6mXb'

access_token = '2890793679-PCdCvWbFTYJ4ZLthc2a5ZXwBONaDW2WKE3wsiLH'
access_token_secret = 'xGUkFNvfP3wkmxxqFDJKzT3BjQrrtOjUGU0LuKFgB2VCM'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def _get_tweet_text():
    while True:
        date, text = random_lines.get_random_lines()
        if text:
            return "{date}\n{text}".format(date=date,text=text)

def send_random_tweet():
    tweet_text = _get_tweet_text()
    if len(tweet_text) <= 140:
        api.update_status(tweet_text)

if __name__ == '__main__':
    send_random_tweet()
