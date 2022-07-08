# Import unofficial twitter API
import twint

class twitter_scrape:
    # def __init__(self, config):
    #     self.config = config
    
    def config(ticker):
        config = twint.Config()
        config.Custom["tweet"] = ["id","created_at","username","tweet","cashtags"]
        config.Store_json = True
        config.Store_object = True
        config.Min_likes = 1000
        config.Search = ticker
        config.Output = "./"+ticker + ".json"
        config.Popular_tweets = True
        config.Lang = "en"

        #Display output to command line bool.
        config.Hide_output = False
        return config

    def run_scrape(self, search):
        twint.run.Search(twitter_scrape.config(search))

def main():
    scrape = twitter_scrape()
    scrape.run_scrape(input('Search: '))

main() 

