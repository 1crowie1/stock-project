# Import unofficial twitter API
import twint

def config(ticker,store_data):
    config = twint.Config()
    config.Search = ticker
    config.Output = ticker + ".csv"
    config.Popular_tweets = True
    config.Store_csv = False
    return config

#Run scrape
twint.run.Search(config(input("Ticker:" ),False))