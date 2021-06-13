'''
extract_article_from_url.py
(c) Geoffrey Karnbach 2021

Extract content of article for specific given URL.
'''

import requests
from bs4 import BeautifulSoup

def get_text_from_url(url, output_file = "sample_input.txt"):

    
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    output = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'code',
        'html',
        'meta',
        'head', 
        'span', 
        'input',
        'style',
        'ul',
        'ol',
        'script',
        'div',
        # there may be more elements you don't want, such as "style", etc.
    ]

    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)

    with open("sample_input.txt","w", encoding="utf8") as f:
        f.write(output)

    return output

def get_title_from_url(url):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    output = ''
    for t in text:
        if t.parent.name == "h1":
            output += '{} '.format(t)

    return output
