## Get started

[Live Demo](https://www.finscrape.com)

To serve the project:

Prerequisites:

- A reddit account and app
- A Supabase account with two tables: crypto_mentions and ticker_mentions. The columns should be set up like so:
  - id (key)
  - created_at
  - ticker
  - comment
  - source
  - sentiment
  - (Optional) A free Heroku account for scheduling cron jobs, you can also simply run the script locally

```bash
pip install supabase pandas dotenv praw stocksymbol requests twilio && pip freeze >> requirements.txt && code .
```

create a .env with the following variables:

```
SUPABASE_URL=supabase-url
SUPABASE_KEY=supabase-anon-key (browser safe)
CLIENT_ID=reddit-app-client-id
SECRET_TOKEN=reddit-app-secret
USERNAME=reddit-username
PASSWORD=reddit-password
```

![alt text](https://i.imgur.com/mV0TSfO.png)

## Scripts breakdown

- ticker-scraper-crypto and reddit do the scraping
- to-csv scripts create a CSV than can be used to create a data visual with Flourish. This script generates a cumulative daily sum. 


