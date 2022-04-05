from dotenv import load_dotenv
import os
from pydantic import conset
import praw
from supabase import create_client, Client
from praw.models import MoreComments
from stocksymbol import StockSymbol
from apscheduler.schedulers.blocking import BlockingScheduler

load_dotenv()  # take environment variables from .env.
#Initialize supabase
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

sched = BlockingScheduler()
@sched.scheduled_job('cron', day_of_week='mon-sun', hour=23)
def scheduled_job():
    # Get all tickers and set the as a list
  api_key = os.environ.get("SYMBOL_KEY")
  ss = StockSymbol(api_key)
  symbol_list_us = ss.get_symbol_list(market="US")
  tickers = []
  for i in range(len(symbol_list_us)):
    tickers.append(symbol_list_us[i]['symbol'])
  tickers_set = set(tickers)

  #Connect to Reddit API via PRAW
  reddit = praw.Reddit(
      client_id=os.environ.get("CLIENT_ID_TANK"),
      client_secret=os.environ.get("SECRET_TOKEN_TANK"),
      user_agent="funpython by u/Tankalele",
      ratelimit_seconds=300
  )

  #Get hot submissions from 3 most popular trading subs / ensure submissions have comments
  urls = []
  url_check = 'comment'
  for submission in reddit.subreddit("superstonk").hot(limit=10):
      if url_check in submission.url:
        urls.append(submission.url)
  for submission in reddit.subreddit("stockmarket").hot(limit=10):
      if url_check in submission.url:
        urls.append(submission.url)
  for submission in reddit.subreddit("pennystocks").hot(limit=10):
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
        for word in words_in_string(tickers_set, comment.body):
          data = supabase.table("ticker_mentions").insert({"ticker": word, 'comment': comment.body}).execute()


sched.start()



