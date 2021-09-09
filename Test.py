import torch
import pandas as pd
import numpy as np
from sklearn import metrics
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer
def metric(true,predict):
    analytics=[]
    #metrics.classification_report(true,predict)
    analytics.append(metrics.accuracy_score(true,predict))
    analytics.append(metrics.precision_score(true,predict,average='weighted'))
    analytics.append(metrics.recall_score(true,predict,average='weighted'))
    analytics.append(metrics.f1_score(true,predict,average='weighted'))
    return analytics
class modelDataset:
    def __init__(self, tokenized_texts):
        self.tokenized_texts = tokenized_texts

    def __len__(self):
        return len(self.tokenized_texts["input_ids"])

    def __getitem__(self, idx):
        return {k: v[idx] for k, v in self.tokenized_texts.items()}
if __name__=='__main__':
    df = ['I like that','That is annoying','This is great!','Wouldn´t recommend it.']
    true=[1,-1,1,-1]
    tokenizer = AutoTokenizer.from_pretrained("siebert/sentiment-roberta-large-english")
    model = AutoModelForSequenceClassification.from_pretrained("siebert/sentiment-roberta-large-english")
    trainer = Trainer(model=model)
    tokenized_texts = tokenizer(df,truncation=True,padding=True)
    pred_dataset = modelDataset(tokenized_texts)
    predictions = trainer.predict(pred_dataset)
    preds = predictions.predictions.argmax(-1)
    preds= [-1 if x == 0 else 1 for x in preds]
    print(metric(true,preds))
