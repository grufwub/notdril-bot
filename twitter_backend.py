import os.path
import sys
import tweepy

class TweetFetcher:
	"""
	Logs in and holds onto Twitter account
	credentials to allow fetching of Tweets
	TODO: don't always hold onto keys and secrets
	"""

	def __init__(self, consumer_key = "", consumer_secret = "", access_key = "", access_secret = ""):
		self._consumer_key = consumer_key
		self._consumer_secret = consumer_secret
		self._access_key = access_key
		self._access_secret = access_secret
		self._auth = None
		self._api = None
		self._login()

	def _login(self):
		self._auth = tweepy.OAuthHandler(self._consumer_key, self._consumer_secret)
		self._api = tweepy.API(self._auth)

	def fetch(self, user = "", since_id = 0, max_id = 0, count = 200):
		return self._api.user_timeline(user, since_id = since_id, max_id = max_id, count = count, tweet_mode = "extended")