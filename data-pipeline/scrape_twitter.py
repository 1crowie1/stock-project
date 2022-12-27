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
        vader_sentiment_array = []
        tb_sentiment_array = []
        subjectivity_sentiment_array = []

        # Go through tweeet rows and check sentiment, print Tweet content,
        # and change sentiment number into categorical data. Add all sentiments into array
        for i, j in tweets.iterrows():
            sen = sentiment.vadersen.sentiment_analysis(j)
            sen2p = sentiment.tbsen.sentiment_analysis_p(j[0])
            sen2s = sentiment.tbsen.sentiment_analysis_s(j[0])
            
            # Adding the values to their arrays so they can be added to pd
            vader_sentiment_array.append(sen)
            tb_sentiment_array.append(sen2p)
            subjectivity_sentiment_array.append(sen2s)

            #Prints for testing 
            print(sentiment.vadersen.sentiment_text(sen))
            print(str(sen2p) + " - Polarity")
            print(str(sen2s) + " - Subjectivity")
            print("Tweet: "+j[0])
            print("Twitter url: https://twitter.com/anyuser/status/"+j[1])
            print()

        # Give an average from the vader array
        print("Average: " + str(sentiment.vadersen.get_avg_sentiment()))

        # Append the sentiment arrays to the original pandas dataframe
        data["sentiment1"] = vader_sentiment_array # Has setting with copy error that needs to be fixed 
        data["sentiment2"] = tb_sentiment_array 
        data["subjectivity"] = subjectivity_sentiment_array

        # Return the new dataframe with tweet sentiment in a new columns
        return data

#Test scrape term 
print(Twitter.scrape("TSLA"))
