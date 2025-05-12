import re

def solid_sign(text):

    text = re.sub(r"([oOgG])[`'‘’´]", r"\1<<SAFE>>", text)

    words_with_apostrophe = re.findall(r"\b\w*[`'‘’´]\w*\b", text)

    cleaned_words = []
    for word in words_with_apostrophe:
        cleaned = re.sub(r"[`'‘’´]", "’", word)
        cleaned_words.append(cleaned)

    return cleaned_words
