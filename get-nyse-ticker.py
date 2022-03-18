from datapackage import Package
from dotenv import load_dotenv
#supase
import os
from supabase import create_client, Client

load_dotenv()  # take environment variables from .env.\










# #Initialize services
# url: str = os.environ.get("SUPABASE_URL")
# key: str = os.environ.get("SUPABASE_KEY")
# supabase: Client = create_client(url, key)

# package = Package('https://datahub.io/core/nyse-other-listings/datapackage.json')

# # print list of all resources:
# print(package.resource_names)

# # send data to supabase
# for resource in package.resources:
#     if resource.descriptor['datahub']['type'] == 'derived/csv':
#         ticker_data = resource.read()
#         for i in ticker_data:
#           print(i[0], i[1])
#           data = supabase.table("nyse_tickers").insert({"ticker":i[0], "company_name":i[1]}).execute()
#           assert len(data.data) > 0