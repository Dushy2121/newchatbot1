import re 
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import pandas as pd 


def processing_data(user_input):

    ps = PorterStemmer()
    l = WordNetLemmatizer()
    corpus = []
    sent = nltk.word_tokenize(user_input)

    for i in range(len(sent)):
        review = re.sub('[^a-zA-Z]', " ", sent[i])
        review = review.lower()
        review = review.split()
        review = [l.lemmatize(word) for word in review if not word in set(stopwords.words("english"))]
        review = " ".join(review)
        corpus.append(review)

    return corpus

def conert_query(processed_data):
    query=" ".join(processed_data)
    return query

def query_new(processed_data):
    dataset=pd.DataFrame({"content":processed_data})
    return dataset

user_input=input()

processed_data=processing_data(user_input)
query_new1=query_new(processed_data)
query=conert_query(processed_data)

print("hi")
print(query)
print(processed_data)
print(query_new1)