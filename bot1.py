import tweepy


class TwitterAPI:
    def __init__(self):
        consumer_key = "mhArS2oEjP7ZkHIWPDgxvXBOc"
        consumer_secret = "zmjQWosjErcMmLNGeZCKsXQxlYKN2Jn0A46HgIb4HfN74Kx8R5"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "3481386493-wnAl5xGfhBSFST6gy92F9vQyTspIwoYCb1Mp5qz"
        access_token_secret = "lrfr2Sr59QEV8tEtAkgigfYRnFx2hishfAhtilwptNG43"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth) # connect to the Twitter API with auth via tweepy

    def tweet(self, message):
        self.api.update_status(status=message) 


           

if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet("Life isn't a matter of milestones, but of moments!")

