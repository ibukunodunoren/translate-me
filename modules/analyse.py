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
    
text = "I really hate this product"
sentence = ["I really hate this product", "but it's also quite interesting to play with"]

pol = analyse(text)
print(pol)
pol = analyse2(sentence)
print(pol)
