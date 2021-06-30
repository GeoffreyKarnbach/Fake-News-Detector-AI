import numpy as np
import pandas as pd
from sklearn.utils import shuffle
import tensorflow as tf
import pickle

def get_model():
    maxlen = 20

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Embedding(100000, 8, input_length=maxlen))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
    
    return model

def train_model(model, df):
    # Shuffle data to improve performance
    df = shuffle(df)
    # Create list from data
    text = []
    for index, rows in df.iterrows():
        wordlist = str(rows["text"])
        text.append(wordlist)

    label = list(df['label'])

    # Create tokenizer
    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=10000)
    tokenizer.fit_on_texts(text)
    sequences = tokenizer.texts_to_sequences(text)
    # Rename for convienience
    x_train = sequences
    y_train = label
    # Preprocess data
    maxlen = 20
    x_train = tf.keras.preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen)

    history = model.fit(np.array(x_train), np.array(y_train),
                    epochs=5,
                    batch_size=8,
                    validation_split=0.2)

    return model, tokenizer

def export_model(model, tokenizer):
    with open('models/tokenizer.pickle', 'wb') as handle:
        pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
    model.save('models/model.h5')