
from dotenv import load_dotenv
#supase
import os
import time
import requests
import praw
from praw.models import MoreComments
from supabase import create_client, Client
import re
load_dotenv()  # take environment variables from .env.

#Initialize services
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


reddit = praw.Reddit(
    client_id=os.environ.get("CLIENT_ID"),
    client_secret=os.environ.get("SECRET_TOKEN"),
    user_agent="python_fun by u/relevant-magic-card",
)

urls = []

for submission in reddit.subreddit("learnpython").hot(limit=10):
    urls.append(submission.url)

submissions = []

for url in urls:
  submissions.append(reddit.submission(url=url))

for submission in submissions:
  for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
      print(comment.body)
      time.sleep(1)




## Setup chrome options
# chrome_options = Options()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome('/root/home/projects/python-ticker-scraper/chromedriver/stable/chromedriver',chrome_options=chrome_options)



