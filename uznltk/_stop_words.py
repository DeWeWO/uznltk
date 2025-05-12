import os

def stop_word():

    path = os.path.join(os.path.dirname(__file__), 'data', 'stopwords_uz.txt')
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

def clean_stop_words(text):
    stopwords = stop_word()
    if isinstance(text, str):
        str_list = text.split()
    else:
        str_list = text
    return [t for t in str_list if t not in stopwords]
