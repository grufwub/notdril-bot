import os.path
import sys
import sqlite3
from datetime import datetime

# Internal Python libraries
from fedi_backend import FediPoster
from twitter_backend import TweetFetcher

### GLOBAL VARIABLES
TWITTER_USER = "dril"
DB_NAME = "tweets_sql.db"

FEDI_KEY = ""
FEDI_SECRET = ""
FEDI_TOKEN = ""

TWITTER_CON_KEY = ""
TWITTER_CON_SECRET = ""
TWITTER_ACC_KEY = ""
TWITTER_ACC_SECRET = ""

# Store Tweets in sqlite db
sql = sqlite3.connect(DB_NAME)
sql_db = sql.cursor()
sql_db.execute('''CREATE TABLE IF NOT EXISTS tweets (tweet_text text, tweet_id varchar(25), tweet_createdat varchar(25)''')

# Setup Fediverse poster
fedi_poster = FediPoster(instance_url = "notbird.site", username = "notdril", client_key = FEDI_KEY, client_secret = FEDI_SECRET, client_token = FEDI_TOKEN)

# Setup Tweet fetcher
tweet_fetcher = TweetFetcher(consumer_key = TWITTER_CON_KEY, consumer_secret = TWITTER_CON_SECRET, access_key = TWITTER_ACC_KEY, access_secret = TWITTER_ACC_SECRET)

### FUNCTIONS
def fetch_tweets(since_id, max_id):
	