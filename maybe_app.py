#basic
#importing essential libraries
from flask import Flask,render_templates, request
import numpy as np
import keras.models
import re
import sys
import os
sys.path.appned(os.path.abspath('./model'))
from load import *
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer

#init flask app
app = flask(__name__)

global model, graph
model, graph = init()

max_words = 50000
max_sequence_len = 250
embedding = 100
filters = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'

# import re
# from nltk.corpus import stopwords
# table = table.reset_index(drop=True)
# REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
# BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
# STOPWORDS = set(stopwords.words('english'))

def process_text(text):
	text = text.str.replace('\d+', '')
	tokenizer = Tokenizer(num_words=max_words, filters=filters, lower=True)
	tokenizer.fit_on_texts(text)
	X = tokenizer.texts_to_sequences(table['title+body'].values)
	X = pad_sequences(X, maxlen=max_sequence_len)
	return X

# def clean_text(text):
#     text = text.lower() # lowercase text
#     text = REPLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text. substitute the matched string in REPLACE_BY_SPACE_RE with space.
#     text = BAD_SYMBOLS_RE.sub('', text) # remove symbols which are in BAD_SYMBOLS_RE from text. substitute the matched string in BAD_SYMBOLS_RE with nothing. 
#     text = text.replace('x', '') # text = re.sub(r'\W+', '', text)
#     text = ' '.join(word for word in text.split() if word not in STOPWORDS) # remove stopwors from text
#     return text

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
	text = request.get_data()
	neat = process_text(text)
	with graph.as_default():
		out = model.predict(neat)
		return out


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host = '0.0.0.0', port=port)	