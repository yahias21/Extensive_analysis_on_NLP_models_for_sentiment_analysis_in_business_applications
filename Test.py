from textblob import TextBlob as tb
from textblob.sentiments import NaiveBayesAnalyzer
from textblob import Blobber
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flair.data import Sentence
from flair.models import TextClassifier
import spacy
from sklearn import metrics
import pandas as pd
# a complete analysis for
def vader(df):
    sentiment=[]
    analyzer = SentimentIntensityAnalyzer()
    for sentence in df:
        vs=analyzer.polarity_scores(sentence)['compound']
        if (vs > 0.5):
            sentiment.append(1)
        elif (vs < -0.5):
            sentiment.append(-1)
        else:
            sentiment.append(0)
    return sentiment
if __name__ == "__main__":
    path="Datasets/usAir_tweets.csv"
    df=pd.read_csv(path)
    trueSent=df["sentiment"].tolist()
    predict=vader(df["text"])
    report=metrics.classification_report(trueSent,predict)
    print(report)