from requests.api import get
import model as m
import pandas as pd

from detection import*
from extract_article_from_url import*

def train():
    df = pd.read_csv("data/kaggle/train.csv")
    model = m.get_model()
    train_model = m.train_model(model, df)
    m.export_model(train_model[0], train_model[1]) 
    model, tokenizer = load_model()
    print(get_prediction(model, tokenizer, "test string")) 

def get_base_input():
    read_ = int(input("Read from sample_input.txt (= 0) or enter link (= 1): "))

    if read_ == 1:
        article = input("Enter article url: ")
        text = get_text_from_url(article)
    else:
        with open("sample_input.txt","r", encoding="utf8") as f:
            text= str(f.readlines())
    get_prediction_from_article(text)

def get_prediction_from_article(text):

    non_fake_coeff, fake_coeff = get_global_coefficient(text)

    try:
        difference = max(non_fake_coeff, fake_coeff)/min(non_fake_coeff, fake_coeff)
    except:
        difference = 1
    
    model, tokenizer = load_model()

    prob_fake_news = get_prediction(model, tokenizer, text)

    non_fake_coeff *= (1-prob_fake_news)
    fake_coeff *= prob_fake_news

    if non_fake_coeff > fake_coeff:
        non_fake = (non_fake_coeff/(non_fake_coeff+fake_coeff))*100/difference
        fake = (fake_coeff/(non_fake_coeff+fake_coeff))*100*difference
        #print(f"Probability of non fake news : {non_fake/(non_fake+fake)*100} %")
        #print(f"Probability of fake news : {fake/(non_fake+fake)*100} %")

        if fake/(non_fake+fake)*100 > non_fake/(non_fake+fake)*100:
            return 0
        else:
            return 1
    else:
        non_fake = (non_fake_coeff/(non_fake_coeff+fake_coeff))*100*difference
        fake = (fake_coeff/(non_fake_coeff+fake_coeff))*100/difference
        #print(f"Probability of non fake news : {non_fake/(non_fake+fake)*100} %")
        #print(f"Probability of fake news : {fake/(non_fake+fake)*100} %")

        if fake/(non_fake+fake)*100 > non_fake/(non_fake+fake)*100:
            return 0
        else:
            return 1


def test_run():
    df = pd.read_csv("data/kaggle/train.csv")
    df = df.iloc[0:200]

    correct = 0
    for index, row in df.iterrows():
        if get_prediction_from_article(str(row["text"])) == row["label"]:
            correct+=1
        print(index)
    print(correct)

if __name__ == "__main__":
    test_run()
    #get_base_input()