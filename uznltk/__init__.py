[tool.poetry]
name = "uznltk"
version = "0.0.8"
description = "description"
authors = ["Ulugbek Salaev"]
om ._download import book_download, news_download
from ._lemmatizer import lemmatize
from ._stem import stem_word
from ._clean import clean_text
from ._ssign import solid_sign
from ._syllable import syllables, hyphenation, count, count_text



# # Faqat funksiyalarni eksport qilamiz
# __all__ = [
#     'stop_word',
#     'clean_stop_words',
#     'lemmatize',
#     'stem_word',
#     'clean_text',
#     'solid_sign',
#     'syllables',
#     'book', 'news', 'hyphenation', 'count', 'count_text', 'split_sentences', 'split_words'
# ]
