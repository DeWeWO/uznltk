import re

def split_sentences(text):
    placeholder_map = {}

    def replace_ip(match):
        key = f"<IP{len(placeholder_map)}>"
        placeholder_map[key] = match.group()
        return key

    text = re.sub(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', replace_ip, text)

    sentences = re.split(r'(?<=[.!?])\s+(?=[A-ZА-ЯЎҚҒЁ])', text.strip())

    restored = [re.sub(r'<IP\d+>', lambda m: placeholder_map[m.group()], s) for s in sentences]

    return [s.strip() for s in restored if s.strip()]


def split_words(text, remove_ip=True, remove_email=True, remove_url=True, remove_emoji=True, remove_punct=True):
    if remove_ip:
        text = re.sub(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', '', text)

    if remove_email:
        text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '', text)

    if remove_url:
        text = re.sub(r'https?://\S+|www\.\S+', '', text)

    if remove_emoji:
        emoji_pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"
            "\U0001F300-\U0001F5FF"
            "\U0001F680-\U0001F6FF"
            "\U0001F1E0-\U0001F1FF"
            "]+", flags=re.UNICODE)
        text = emoji_pattern.sub(r'', text)

    if remove_punct:
        text = re.sub(r'[^\w\sʼ’ʻ\-]', '', text)

    tokens = re.findall(r'\b[\wʼ’ʻ\-]+\b', text)

    cleaned = []
    for token in tokens:
        if re.fullmatch(r'(milodiy\s*)?\d{4}[- ]?(yil|y\.?)?(dan|ga|da|ni|ning)?', token.lower()):
            cleaned.append(token)
        elif token.isdigit():
            continue
        elif re.fullmatch(r'[a-zA-Zа-яА-ЯёЁʼ’ʻ\-]+', token):
            cleaned.append(token)

    return cleaned
