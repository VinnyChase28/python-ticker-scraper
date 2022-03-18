from dotenv import load_dotenv
#supase
import os
import time
from supabase import create_client, Client
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
load_dotenv()  # take environment variables from .env.

#Initialize services
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/root/home/projects/python-ticker-scraper/chromedriver/stable/chromedriver',chrome_options=chrome_options)

#Set webdriver

driver.get('https://cloudbytes.dev')

#Get content
description = driver.find_element(By.NAME, "description").get_attribute("content")
print(f"{description}")



# Write to Supabase - working
# data = supabase.table("nyse_mentions").insert({"ticker":"SPY"}).execute()
# assert len(data.data) > 0

