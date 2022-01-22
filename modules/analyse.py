from textblob import TextBlob

# Performs sentiment analysis on a message and returns the sentiment rounded to 2dp
def analyse(text):
    return round(TextBlob(text).sentiment.polarity, 2)

# input an array of text
def analyse2(sentence):
    polarity = 0
    for slice in sentence:
        polarity += TextBlob(slice).sentiment.polarity
        
    return round(polarity/len(sentence), 2)
