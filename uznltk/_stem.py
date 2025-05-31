from UzMorphAnalyser import UzMorphAnalyser

# Avval obyekt yaratish kerak
analyser = UzMorphAnalyser()
def stem_word(word):
    # So‘zni lemmatizatsiya qilish
    a=analyser.stem(word)
    return a

