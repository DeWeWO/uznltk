import re

def clean_text(text):
    apostrophes = ["'", "`", "‘", "’", "´"]

    pattern = r"[`'‘’´]"
    text = re.sub(pattern, "’", text)

    for a in apostrophes:
        text = text.replace(f"o{a}", "o‘")
        text = text.replace(f"g{a}", "g‘")
        text = text.replace(f"O{a}", "O‘")
        text = text.replace(f"G{a}", "G‘")

    return text

def solid_sign(text):

    text = re.sub(r"([oOgG])[`'‘’´]", r"\1<<SAFE>>", text)

    words_with_apostrophe = re.findall(r"\b\w*[`'‘’´]\w*\b", text)

    cleaned_words = []
    for word in words_with_apostrophe:
        cleaned = re.sub(r"[`'‘’´]", "’", word)
        cleaned_words.append(cleaned)

    return cleaned_words
