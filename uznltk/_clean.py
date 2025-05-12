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