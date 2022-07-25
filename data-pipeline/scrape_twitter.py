import twint
import pandas as pd

class Twitter:
    def scrape(search):
        c= twint.Config()
        c.Search= search
        c.Lang="en"
        c.Pandas= True
        c.Limit= 30
        c.Popular_tweets = True
        c.Hide_output = True
        c.Min_likes = 100

        twint.run.Search(c)

        def twint_to_pd(columns):
            return twint.output.panda.Tweets_df[columns]
        
        data= twint_to_pd(["id","created_at","username","tweet","cashtags"])
        #data["tweet"]= data["tweet"].str.replace("[^a-zA-Z0-9]", " ")
        
        return(data)
