import tweepy
import pandas as pd

# Replace with your own Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def get_tweets(query, count):
    tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en").items(count):
        tweets.append(tweet.text)
    return tweets

# Example usage
if __name__ == "__main__":
    tweets = get_tweets('Bitcoin', 100)
    df = pd.DataFrame(tweets, columns=['tweet'])
    df.to_csv('data/bitcoin_tweets.csv', index=False)
