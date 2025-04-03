import os
import tweepy
import time

API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def load_tweets(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File {file_path} not found.")
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

def main():
    tweet_file = "tweets.txt"
    tweets = load_tweets(tweet_file)
    index = 0

    while True:
        if not tweets:
            print("⚠️ No tweets loaded. Waiting 15 minutes and retrying.")
        else:
            tweet = tweets[index % len(tweets)]
            try:
                api.update_status(tweet)
                print(f"✅ Tweet sent: {tweet}")
            except Exception as e:
                print(f"❌ Failed to tweet: {e}")
            index += 1
        time.sleep(900)

if __name__ == "__main__":
    main()