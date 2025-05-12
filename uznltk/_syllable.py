def syllables(text):
    tokens = processing(text)
    sylls = list()
    for token in tokens:
        count = 0
        vowels = set("AaEeUuOoIiАаОоУуИиЯяЕеЁёЮюЭэЎў")
        syll = list()
        start = 0
        for letter in token:
            for i in range(65, 91):
                if ord(letter) == i:
                    count += 1
            for i in range(1040, 1072):
                if ord(letter) == i:
                    count += 1
        if count > 1:
            sylls.append(token)
            continue
        count = 0
        for letter in token:
            if letter in vowels:
                count += 1
        if count == 1:
            sylls.append(token)
            continue
        for i in range(2, len(token)):
            if token[i] in vowels and token[i - 1] not in vowels:
                w = token[start: i - 1]
                if len(w) != 0:
                    syll.append(w)
                    start = i - 1
            if token[i] in vowels and token[i - 1] in vowels:
                w = token[start: i]
                if len(w) != 0:
                    syll.append(w)
                    start = i
        w = token[start:len(token)]
        syll.append(w)
        count = 0
        for i in syll[0]:
            if i in vowels:
                count += 1
        if count == 0:
            s = syll[1]
            syll[1] = syll[0]+s
            syll[0] = ""
        if count == 2:
            s = syll[0]
            syll.remove(syll[0])
            temp = list()
            start = 0
            for i in range(1, len(s)):
                if s[i] in vowels and s[i - 1] in vowels:
                    w = s[start: i]
                    if len(w) != 0:
                        temp.append(w)
                        start = i
                w = s[start:len(s)]
                temp.append(w)
            syll = temp + syll
        while len(''.join(syll)) != len(token):
            d = ''
            for i in range(1, len(syll)):
                s = ''.join(syll)
                if syll[i] == syll[i-1] and s != token:
                    d = syll[i]
            syll.remove(d)
        for i in range(1, len(syll)):
            if syll[i][0] == 'h' or syll[i][0] == chr(8216):
                if syll[i-1][len(syll[i-1])-1] in ['s', 'c'] or syll[i][0] == chr(8216):
                    s = syll[i]
                    syll[i] = syll[i-1][len(syll[i-1])-1] + s
                    s = syll[i-1]
                    syll[i-1] = s[0:len(s)-1]
        for i in range(1, len(syll)):
            if syll[i][0] == 'g' and syll[i][1] != chr(8216) and len(syll[i-1]) > 0:
                if syll[i-1][len(syll[i-1])-1] == 'n':
                    s = syll[i]
                    syll[i] = syll[i-1][len(syll[i-1])-1] + s
                    s = syll[i-1]
                    syll[i-1] = s[0:len(s)-1]
        str = ""
        for w in syll:
            if len(w) > 1 and w[len(w)-1] == '-':
                w = w[0:len(w)-1]
            if len(w) > 1 and w[0] == '-':
                w = w[1:len(w)]
            if w != '':
                str += w
                if not w.__contains__('-'):
                    str += '-'
        sylls.append(str[0:len(str)-1])
    return sylls
def processing(text):
    text = str(text)
    text = text.replace("`", "'")
    text = text.replace("O'", "O‘").replace("o'", "o‘").replace("G'", "G‘").replace("g'", "g‘").replace("'", "’")
    return text.split()
def hyphenation(text):
    word = text
    syllable = ' '.join(syllables(text))
    begin = end = ''
    if word.__contains__('-'):
        for i in range(0, len(word)):
            if word[i] == '-':
                begin = word[i - 1]
                end = word[i + 1]
    lines = list()
    if not syllable.__contains__('-'):
        lines.append(syllable)
    tokens = syllable.split('-')
    count = len(tokens) - 1
    for j in range(1, len(tokens)):
        if len(tokens[j]) != 1:
            w = ''
            for i in range(0, j):
                w += tokens[i]
            if len(tokens[j - 1]) != 1 and not tokens[j - 1].__contains__(chr(8217)):
                w += '-'
            for i in range(j, len(tokens)):
                if len(tokens[i]):
                    w += tokens[i]
            if begin != end != '' and len(end):
                for i in range(0, len(w) - 1):
                    if w[i] == begin and w[i + 1] == end:
                        w = w[0:i + 1] + '-' + w[i + 1:len(w)]
                        break
            if w != word or count == 1 or word.__contains__('-') and w not in lines:
                lines.append(w)
    return lines
def count(text):
    tokens = syllables(text)
    count = 0
    for token in tokens:
        syll = token.split('-')
        count += len(syll)
    return count
def count_text(text: str) -> int:
    return len(text)