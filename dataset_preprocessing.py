import pandas as pd

if __name__ == '__main__':
    # path of csv file
    Path = "twitters1.csv"
    # # open csv file
    # df=pd.read_csv(Path)
    # df = df.drop('indezs', 1)
    # # filter columns
    # filterC = df["airline_sentiment", "text","sentiment"]
    # # # filter rows
    # # thresh=df["airline_sentiment_confidence"]>=0.5
    # # filterR=filterC[thresh]
    # #remove substrings
    # for ind in range(df['text'].shape[0]):
    #     s = str(df['text'].at[ind])
    # #     strs = s.split()
    # #     m = " ".join([x for x in strs if not x.startswith('@')])
    # #     df['text'].at[ind]=m
    # df.drop('Unnamed: 0', inplace=True, axis=1)
    # #     # save csv file
    # df.to_csv("twitters1.csv")
    # f = open("test.csv", "w")
    #
    # for i in range():
    #     f.write("{} {}\n".format(bins[i], freq[i]))
    #
    # f.close()
    # for ind in range(df['text'].shape[0]):
    #     s=df['airline_sentiment'].at[ind]
    #     if s=='positive':
    #         df['sentiment'].at[ind]=1
    #     elif s=='negative':
    #         df['sentiment'].at[ind]=-1
    #     elif s=='neutral':
    #         df['sentiment'].at[ind]=0
    # df.to_csv("twitters1.csv",index=False)

    # # # spacy part
    # # nlp = spacy.load("en_core_web_sm")
    # # load packages
    # from sklearn.feature_extraction.text import TfidfVectorizer
    # import math
    # # calculate the # of unique words in the corpus
    # feature = []
    # for i in df["patterns"]:
    #     feature.append(i.split())
    #     flat_list = [item for items in feature for item in items]
    #     feature=len(set(flat_list))
    # # only take the top 10% of the most frequent words
    # # set the max document frequency to 0.2 to maintain the uniqueness
    # max_feature = math.ceil(feature*0.1)
    # tfidfvectoriser=TfidfVectorizer(strip_accents="ascii",
    #                                 max_features=max_feature,
    #                                 max_df = 0.2)
    # tfidfvectoriser.fit(df["patterns"])
    # tfidf_vectors=tfidfvectoriser.transform(df["patterns"])
    # tfidf_vectors=pd.DataFrame(tfidf_vectors.toarray())
    # tfidf_vectors.columns = tfidfvectoriser.get_feature_names()
    # # merge the words into the original table
    # customer = pd.merge(customer,
    #                     tfidf_vectors,
    #                     left_index=True,

    # df.drop_duplicates(subset =”Description”, keep = “first”, inplace = True)
    # df['Description'] = df['Description'].astype('str')
    # df['Sentiment_Type']=''
    # df['Polarity'] = df['Description'].apply(get_polarity)
    # df.loc[df.Polarity>0,'Sentiment_Type']='POSITIVE'
    # df.loc[df.Polarity==0,'Sentiment_Type']='NEUTRAL'
    # df.loc[df.Polarity<0,'Sentiment_Type']='NEGATIVE'
    # df.Sentiment_Type.value_counts().plot(kind='bar',title="Sentiment Analysis")
    # df['compound'] = df['scores'].apply(lambda score_dict: score_dict['compound'])
    # df['scores'] = df['Description'].apply(lambda Description: sid.polarity_scores(Description))
    # df['sc ores'] = df['review'].apply(lambda review: sid.polarity_scores(review))