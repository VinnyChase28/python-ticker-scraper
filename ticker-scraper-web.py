from dotenv import load_dotenv
#supase
import os
import time
import requests
from bs4 import BeautifulSoup
from supabase import create_client, Client
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import re
load_dotenv()  # take environment variables from .env.

#Initialize services
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
auth = requests.auth.HTTPBasicAuth(os.environ.get('CLIENT_ID'), os.environ.get('SECRET_TOKEN'))
# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': os.environ.get("USERNAME"),
        'password': os.environ.get("PASSWORD")}

headers = {'User-Agent': 'MyBot/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

res = requests.get("https://oauth.reddit.com/r/python/hot",
                   headers=headers)

for post in res.json()['data']['children']:
  print(post['data']['title'])