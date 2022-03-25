from dotenv import load_dotenv
#supase
import os
import time
import requests
from bs4 import BeautifulSoup
from supabase import create_client, Client
import scrapy
import pandas as pd
import re
import logging
load_dotenv()  # take environment variables from .env.

#Initialize services
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


class ListaDeCursosSpider(scrapy.Spider):
    name = "lista_de_cursos"
    allowed_domains = ['www.coursetalk.com']
    start_urls = ['https://www.coursetalk.com/subjects/data-science/courses/'] 

    def parse(self, response):
            logging.info("response.status:%s"%response.status)
            logourl = response.selector.css('div.main-nav__logo img').xpath('@src').extract()
            logging.info('response.logourl:%s'%logourl)