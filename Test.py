from textblob import TextBlob as tb
from textblob.sentiments import NaiveBayesAnalyzer
from textblob import Blobber
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flair.models import TextClassifier
from flair.data import Sentence
import spacy


# a complete analysis for
if __name__ == "__main__":
    # VADER PART
    analyzerV = SentimentIntensityAnalyzer()
    sentence="the party is savage, i enjoy thr"
    vs=analyzerV.polarity_scores(sentence)['compound']
    print(vs)
    # # FLAIR PART
    # classifierF = TextClassifier.load('en-sentiment')
    # sentence=Sentence('')
    # classifierF.predict(sentence)
    # print(sentence.labels)
    # # TEXTBLOB PART "Pattern"
    # ts=tb("the party was pretty bad").polarity
    # print(ts)
    # # nltk.download('punkt')
    # # textblob_Naivebayes
    # tb = Blobber(analyzer=NaiveBayesAnalyzer())
    # ts=tb("the party was pretty bad").sentiment
    # print(ts[2])
    # # # spacy part
    # # nlp = spacy.load("en_core_web_sm")