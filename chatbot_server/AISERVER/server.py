#python server libs
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

#ai
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


#web server
app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello_world():
	return 'Hello World'

@app.route('/process-text',methods=['POST'])
def process_image():
    try:
        data = request.json
        processed_data = processing_data(data["message"])
        return {"status:":"true","data":processed_data}
    except error:
        return {"status:":"false","error":error}

if __name__ == '__main__':
	app.run()
