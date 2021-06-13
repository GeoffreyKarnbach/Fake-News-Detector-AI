'''
most_important_words.py
(c) Geoffrey Karnbach 2021

From a specific text file, exporting the most important words. Decided by occurence, length, coefficient decided by length and coefficient depending on word.
Simply add text in sample_input.txt and execute the program.
'''

import math

def coefficient_by_length(length):
    value = math.exp(length/3)-2
    if value <=0.5:
        return 0.5
    return value

def coefficient_by_word(word):
    # Load from DB
    # If UPPERCASE increase
    return 1

def get_lead_keywords():
     
    with open("sample_input.txt","r", encoding="utf8") as f:
        content = f.read()

    to_replace = ["\n", "(","-",")","\“",".",",",":","  "]
    for loop in to_replace:
        content = content.replace(loop," ")

    all_words = {}
    for word in content.split(" "):
        if word in all_words:
            all_words[word]+=1
        else:
            all_words[word]=1

    all_words = dict(reversed(sorted(all_words.items(), key=lambda item: item[1]))) 
    nb_words = len(all_words)

    words_valued = {}
    for id, words in enumerate(all_words.keys()):
        words_valued[words] = int(all_words[words]*len(words)*coefficient_by_length(len(words))*coefficient_by_word(words))

    for loop, word in enumerate(dict(reversed(sorted(words_valued.items(), key=lambda item: item[1]))).keys()):
        if loop  < (nb_words/20):
            print(word)
    

def get_keyword_from_title(title):
    all_words = {}
    for word in title.split(" "):
        if len(word) != 0:
            all_words[word] = len(word)

    all_words = dict(reversed(sorted(all_words.items(), key=lambda item: item[1]))) 
    nb_words = len(all_words)
    keyword_amount = math.floor(nb_words*0.7)


    all_keywords = []

    for loop, word in enumerate(all_words):
        if loop  < keyword_amount:
            all_keywords.append(word)
    
    for word in title.split(" "):
        if word in all_keywords:
            print(word, end = " ")
    
    print()

if __name__ == "__main__":
    from extract_article_from_url import*
    url = input("Enter link to article: ")
    print("=== Body keywords ===")
    get_text_from_url(url)
    get_lead_keywords()
    print("=== Title keywords ===")
    get_keyword_from_title(get_title_from_url(url))
