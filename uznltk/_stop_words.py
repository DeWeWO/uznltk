import requests

def stop_words_list():
    """Stopwords ro'yxatini GitHub'dan yuklab oladi"""
    url = "https://raw.githubusercontent.com/DeWeWO/uznltk_data/master/stopwords_uz.txt"
    response = requests.get(url)
    response.raise_for_status()
    return [w.strip() for w in response.text.splitlines() if w.strip()]

def clear_stopword(text):
    """Berilgan matndan stopwords ni olib tashlaydi"""
    stopwords = set(stop_words_list())
    words = text.split()
    filtered = [w for w in words if w.lower() not in stopwords]
    return ' '.join(filtered)
