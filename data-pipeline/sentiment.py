from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as sentiment

# Sentiment analysis function
def sentiment_analysis(data): 
    for sentence in data:
        vs = sentiment().polarity_scores(sentence)
        return(vs['compound'])

avg_sentiment_array = []

def Average(lst):
    return sum(lst) / len(lst)

def get_avg_sentiment():
    return Average(avg_sentiment_array)

# Add categorical sentiment to the returned value
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


