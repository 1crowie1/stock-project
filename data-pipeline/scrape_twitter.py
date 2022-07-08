# Import unofficial twitter API
import twint

def config(ticker: str, store_data: bool) -> twint.Config:
    config = twint.Config()
    config.Search = ticker
    config.Output = ticker + ".csv"
    config.Popular_tweets = True
    config.Store_csv = False
    return config

#Run scrape
def scrape_tweets() -> dict:
    twint.run.Search(config(input("Ticker:" ),False))