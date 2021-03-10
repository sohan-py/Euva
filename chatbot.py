from textblob import *
from random import choice
import mysql_utils as mysql
from intents import intents
from datefinder import find_dates
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

def clean_sentence(sentence):
    cleaned_sentence = ''
    sentence = Sentence(sentence)
    sentence = sentence.lower().words
    sentence.sort()
    for word in sentence:
        cleaned_sentence += word.lemmatize() + ' '
    return Sentence(cleaned_sentence.strip())

def score(sentences):
    for i in range(len(sentences)):
        sentences[i] = str(clean_sentence(sentences[i]))
    x = vectorizer.fit_transform(sentences).toarray()
    return cosine_similarity([x[0]], [x[1]])

def response(message, userinfo):
    dates = [date for date in find_dates(message)]
    journal = mysql.journal_from_dates(userinfo['id'], dates)
    if not journal is None:
        return journal, True
    max_score = 0
    best_class = {}
    for intent in intents():
        for pattern in intent['patterns']:
            pattern = str(clean_sentence(pattern))
            curr_score = score([message, pattern])[0][0]
            if curr_score > max_score:
                max_score = curr_score
                best_class = intent
    if max_score == 0:
        best_class = intents()[-1]
    if best_class['tag'] in list(userinfo.keys()):
        response = choice(best_class['responses']).replace('<' + best_class['tag'] + '>', userinfo[best_class['tag']])
    else:
        response = choice(best_class['responses'])
    return response, False
