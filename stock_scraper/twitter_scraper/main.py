# Import unofficial twitter API
import twint

#Test configuration
config = twint.Config()
config.Search = "$APPL"
config.Output = "appl.csv"
config.Popular_tweets = True

#Turn saving into a csv on or off
config.Store_csv = False

#Run scrape
twint.run.Search(config)