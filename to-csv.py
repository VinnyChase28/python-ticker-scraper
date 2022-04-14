from dotenv import load_dotenv
import os
from supabase import create_client, Client
import pandas as pd

load_dotenv()  # take environment variables from .env.
#Initialize supabase
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
data = supabase.table("ticker_mentions").select("created_at, ticker" ).execute()

to_list = list(data)
real_data = to_list[0]
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct["data"]


test = Convert(real_data)
# get all unique tickers
print(test[:10])
tickers = []
for i in test:
  tickers.append(i["ticker"])
tickerset = list(set(tickers))
tickerset.sort()
#get all unique dates
dates = []
for i in test:
  dates.append(i["created_at"].rpartition('T')[0])
dateset = list(set(dates))
dateset.sort()

#create a csv using pandas and increment the cell intersection by 1 each time
df = pd.DataFrame(index=tickerset, columns=dateset)
df.loc[:,:] = 0

for i in test:
  h = i['ticker']
  j = i['created_at'].rpartition('T')[0]
  if h in tickerset and j in dateset:
      df.loc[h,j] += 1

print(df)
df.to_csv(path_or_buf='test.csv')