import pandas as pd
import streamlit as st
import requests
import json
import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def run():
    #widget input
    st.title("Spotify Reviews Sentiment")
    review = st.text_input('Masukkan Review Anda',value="", max_chars=150)

    # input to dataframe
    new_data = {'Review': review}
    new_data1 = pd.DataFrame([new_data])

    # preprocessing
    # # Make a function of text preprocessing

    nltk.download('all')

    def clean_rev(rev):

        # make text lowercase
        rev = rev.lower()

        # remove text in bracket
        rev = re.sub('\[.*?\]', '', rev)

        # remove punctuation
        rev = re.sub('[%s]' % re.escape(string.punctuation), '', rev)

        # remove words containing numbers
        rev = re.sub('\w*\d\w*', '', rev)

        # remove non-latin words
        rev = re.sub('[^\x00-\x7f]', '', rev)

        # remove non-words (emoji, etc.)
        rev = re.sub("[^A-Za-z\s']", " ", rev)

        # remove underscores
        rev =  str.replace(rev, '_', '')

        # remove whitespace
        rev = rev.strip()

        # Tokenization
        tokens = word_tokenize(rev)

        # Remove Stopwords
        stop_words = set(stopwords.words('english'))
        stop_words.remove('not')
        rev = [word for word in tokens if word not in stop_words]

        # Lemmatize the word
        sentence = []
        for word in rev:
            lm = WordNetLemmatizer()
            sentence.append(lm.lemmatize(word, 'v'))

        return ' '.join(sentence)

    new_data1= new_data1['Review'].apply(lambda x: clean_rev(x))

    new_data1= new_data1.tolist()

    # input ke model
    input_data_json = json.dumps({
            "signature_name": "serving_default",
            "instances": new_data1

    })

    # inference
    URL = "http://spotify-afifah.herokuapp.com/v1/models/model_spotify:predict"
    r = requests.post(URL, data=input_data_json)

    if r.status_code == 200:
        res = r.json()
        if res['predictions'][0][0] >= 0.5:
            st.write('Sentiment of Your Review : Good')
        else:
            st.write('Sentiment of Your Review : Bad')
    else:
        st.write('Error')

if __name__ == '__main__':
    run()