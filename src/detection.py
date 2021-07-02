from name_recognition import get_human_names
import math
import tensorflow as tf
import pickle
import numpy as np

def get_exclamation_coefficient(text):
    # In average, with training data set, (2 times more ! for fake than non fake news) but only 1 in 3 articles (fake news) had !
    amount = text.count("!")   
    return (amount/2, 0.3*amount**2+0.9)

def get_total_length_coefficient(text):
    total_length = len(text) / 500
    fake = max(-13659040 + (2154.389 -  -13659040)/(1+(total_length/73864090000)**(0.3929395)),0)/2000
    non_fake = max(-8*(total_length-11)**2+800,0)/2000
    return (non_fake, fake) 

def get_global_coefficient(text):
    fake_coeff = 0
    non_fake_coeff = 0

    # Coefficient by exclamation point
    exclam_coeff = get_exclamation_coefficient(text)
    non_fake_coeff += exclam_coeff[0]
    fake_coeff += exclam_coeff[1]

    # Coefficient by total text length
    total_length_coeff = get_total_length_coefficient(text)
    non_fake_coeff += total_length_coeff[0]
    fake_coeff += total_length_coeff[1]

    # Coefficient by amount of names
    amount_names = get_human_names(text)

    fake_coeff += (1.2/math.exp(amount_names)+0.5)*4
    non_fake_coeff += max((-2*((amount_names-15)**2)+150)*4,0) # Geogebra value 0 for 18

    # Output
    return (non_fake_coeff,fake_coeff)
    
def load_model():
    model = tf.keras.models.load_model("models/model.h5")
    with open('models/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    return model, tokenizer

def get_prediction(model, tokenizer, text):
    data = tf.keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=20)
    # Predict using model
    result = model.predict(np.array(data))[0][0]
    return result