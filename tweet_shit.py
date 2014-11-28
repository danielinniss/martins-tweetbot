import tweepy
import random_lines
import access_details

auth = tweepy.OAuthHandler(access_details.consumer_key, access_details.consumer_secret)
auth.secure = True
auth.set_access_token(access_details.access_token, access_details.access_token_secret)
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
