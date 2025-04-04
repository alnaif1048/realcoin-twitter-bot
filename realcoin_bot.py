
import tweepy
import time
import os

# مصادقة تويتر باستخدام المفاتيح البيئية
auth = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_API_KEY"),
    os.getenv("TWITTER_API_SECRET"),
    os.getenv("TWITTER_ACCESS_TOKEN"),
    os.getenv("TWITTER_ACCESS_SECRET")
)

api = tweepy.API(auth)

# تحميل التغريدات من ملف خارجي
with open("tweets.txt", "r", encoding="utf-8") as file:
    tweets = [line.strip() for line in file if line.strip()]

# بدء التغريد كل 15 دقيقة
while True:
    for tweet in tweets:
        try:
            api.update_status(tweet)
            print(f"✅ تم نشر التغريدة: {tweet}")
            time.sleep(900)  # 15 دقيقة
        except Exception as e:
            print(f"❌ خطأ أثناء النشر: {e}")
            time.sleep(60)  # انتظر دقيقة قبل المحاولة مجددًا
