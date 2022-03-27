from turtle import clear
from dotenv import load_dotenv
import os
import praw
from supabase import create_client, Client
from praw.models import MoreComments
import json
from bs4 import BeautifulSoup
import requests 

load_dotenv()  # take environment variables from .env.
#Initialize supabase
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


# Get all cryptos and set the as a list

crypto_list = []

url = 'https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

for start in range(1, 20000, 5000):

    params = {
        'start': start,
        'limit': 5000,
    }

    r = requests.get(url, params=params)
    data = r.json()
    
    for number, item in enumerate(data['data']):
        crypto_list.append(item['symbol'])


crypto_list_set = set(crypto_list)
print(crypto_list_set) 

#Connect to Reddit API via PRAW
reddit = praw.Reddit(
    client_id=os.environ.get("CLIENT_ID_TWO"),
    client_secret=os.environ.get("SECRET_TOKEN_TWO"),
    user_agent="WSBetter by u/relevant-magic-card",
    ratelimit_seconds=300
)

#Get hot submissions from 3 most popular trading subs / ensure submissions have comments
urls = []
url_check = 'comment'
for submission in reddit.subreddit("cryptocurrency").hot(limit=10):
    if url_check in submission.url:
      urls.append(submission.url)
for submission in reddit.subreddit("cryptomarkets").hot(limit=10):
    if url_check in submission.url:
      urls.append(submission.url)
for submission in reddit.subreddit("cryptocurrencies").hot(limit=10):
    if url_check in submission.url:
      urls.append(submission.url)

submissions = []
for url in urls:
  submissions.append(reddit.submission(url=url))
print(submissions)

#Send to Supabase
def words_in_string(word_list, a_string):
    return set(word_list).intersection(a_string.split())
for submission in submissions:
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
      for word in words_in_string(crypto_list_set, comment.body):
        data = supabase.table("crypto_mentions").insert({"ticker": word, 'comment': comment.body, 'source': 'reddit'}).execute()