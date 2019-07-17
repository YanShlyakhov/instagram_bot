
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import pickle
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential

def restore_model():
    # load our saved model
    model = load_model('my_model.h5')
    # load tokenizer
    tokenizer = Tokenizer()
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    return model, tokenizer

def predict(text):
    x_data_series = pd.Series([text])
    x_tokenized = tokenizer.texts_to_matrix(x_data_series, mode='tfidf')
    prediction = model.predict(np.array(x_tokenized))
    return prediction[0]

# These are the labels we stored from our training
# The order is very important here.
 
labels = np.array(['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc',
 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x',
 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball',
 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space',
 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast',
 'talk.politics.misc', 'talk.religion.misc'])

model, tokenizer = restore_model()

if __name__ == "__main__":
    # Это просто вектор
    prediction = predict("To pass the levels you have to travel through the the wormholes, enter the orbits of the planets, resist gravity or follow it. The atmosphere of the game is ideal to relax and rest after a hard day, to pass the time, at the same time not badly stretching its logic.")
    #print("kek")
    #print(labels[np.argmax(prediction))

    print(prediction)

