from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as sentiment
from textblob import TextBlob

avg_sentiment_array = []

def Average(lst):
    return sum(lst) / len(lst)
    
class tbsen:
    # this could probably be simplified into one function ...
    #Textblob returns two values p - polaity & s - subjectivity
    def sentiment_analysis_p(data):
        tbsentiment = TextBlob(data)
        return tbsentiment.sentiment[0]
        # Returns polarity -1 = Negative & +1 = Positive
    
    def sentiment_analysis_s(data):
        tbsentiment = TextBlob(data)
        return tbsentiment.sentiment[1]
        # Returns objectivity 0 = Very Objective & 1 = Very Subjective
class vadersen:
    # Sentiment analysis function
    def sentiment_analysis(data): 
        for sentence in data:
            vadersentiment = sentiment().polarity_scores(sentence)
            return(vadersentiment['compound'])

    def get_avg_sentiment():
        return Average(avg_sentiment_array)

    # Add categorical sentiment to the returned value for testing
    def sentiment_text(sen):
        if sen >= 0.05:
            avg_sentiment_array.append(sen)
            return str(sen) + " - Positive"
        elif sen <= -0.05:
            avg_sentiment_array.append(sen)
            return str(sen) + " - Negative"
        elif sen > -0.05 or sen <0.05:
            avg_sentiment_array.append(sen)
            return str(sen) + " - Neutral"


