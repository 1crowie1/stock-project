# Import unofficial twitter API
import twint

def config(ticker,store_data):
    config = twint.Config()
    config.Custom["tweet"] = ["id","created_at","username","tweet","cashtags"]
    config.Store_json = True
    config.Store_object = True
    config.Min_likes = 1000
    config.Search = ticker
    config.Output = "./"+ticker + ".json"
    config.Popular_tweets = True
    config.Lang = "en"
    return config

#Run scrape
twint.run.Search(config(input("Search: " ),False))
