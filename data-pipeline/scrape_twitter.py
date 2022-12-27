import twint
import pandas as pd
import sentiment

class Twitter:
    def scrape(search):
        c= twint.Config()
        c.Search= search
        c.Lang="en"
        c.Pandas= True
        c.Limit= 10
        c.Popular_tweets = True
        c.Hide_output = True
        c.Min_likes = 100

        twint.run.Search(c)

        def twint_to_pd(columns):
            return twint.output.panda.Tweets_df[columns]
    
        #Change response from twint into pandas dataframe
        data = twint_to_pd(["id","created_at","username","tweet","cashtags"])

        #Extract tweet and id to analyse sentiment
        tweets = twint_to_pd(["tweet", "id"])
        sentiment_array = []

        # Go through tweeet rows and check sentiment, print Tweet content,
        # and change sentiment number into categorical data. Add all sentiments into array
        for i, j in tweets.iterrows():
            sen = sentiment.sentiment_analysis(j)
            print(sentiment.sentiment_text(sen))
            sentiment_array.append(sen)
            print("Tweet: "+j[0])
            print("Twitter url: https://twitter.com/anyuser/status/"+j[1])
            print()

        # Append the sentiment array to the original pandas dataframe and give an average
        # this is mostly for testing. 
        print("Average: " + str(sentiment.get_avg_sentiment()))

        data["sentiment"] = sentiment_array # Has setting with copy error that needs to be fixed 
        

        # Return the new dataframe with tweet sentiment in a new column
        return data

#Test scrape term 
print(Twitter.scrape("MSFT"))
