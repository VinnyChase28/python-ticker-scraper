from dotenv import load_dotenv
import os
from supabase import create_client, Client
from stocksymbol import StockSymbol
load_dotenv()  # take environment variables from .env.
#Initialize supabase
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
## get all tickers
api_key = os.environ.get("SYMBOL_KEY")
ss = StockSymbol(api_key)
symbol_list_us = ss.get_symbol_list(market="US")
tickers = []
for i in range(len(symbol_list_us)):
  tickers.append(symbol_list_us[i]['symbol'])
#push tickers to supabase
for i in range(len(tickers)):
  data = supabase.table("tickers").update({"symbol":tickers[i]}).eq("symbol", tickers[i]).execute()