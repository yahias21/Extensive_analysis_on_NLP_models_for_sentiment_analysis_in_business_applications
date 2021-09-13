# Extensive analysis on NLP models for sentiment analysis in business applications
![picture](https://media.springernature.com/original/springer-static/image/chp%3A10.1007%2F978-981-15-0029-9_7/MediaObjects/475950_1_En_7_Fig2_HTML.png)
## Models Ideas:
1. Use of custom models for different categories (tech, food, books,...) to be automatically (using context classfication) or manually selected(by the client). *(different datasets applied)*
2. Run multiple models per dataset and derive weighted average results.
3. Developing a layered classification **use *fast/slow* classification** (divide the dataset using confidence index to strong and weak groups; the weak group will be analysed further using Roberta model).
4. Aspect based analysis **(attach sentiment to specific aspects rather than sentence/opinion)** and word cloud **(for word frequencies)** to show insights of the reviews. (Amazon comprehend model)
5. Use of lemmatization, opinion unit extractor, subjectivity index and multiclass classification(love, sad, angry,...) for better accuracy and data enrichment.
6. Test of a sent-ngrams lexion sentiment analysis **(SO-CAL)**.
7. Use of client dataset to fine-tune the model. (Ideation phase)
## Datasets used:
1. Twitter airline 
2. IMDB 
3. Yelp (preprocessing phase)
4. Amazon 
5. 140sentiment twitter
## Models used:
1. Textblob
2. Flair (RNN)
3. Vader
4. Roberta-large
5. Bert_multilingual
## Results:
<a href="https://drive.google.com/uc?export=view&id=<1ZTzuKZz2BD2dHE5T5U2jPtkXjfjpGAyu>"><img src="https://drive.google.com/uc?export=view&id=<FILEID>" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />
