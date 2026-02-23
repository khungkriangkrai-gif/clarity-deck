import random
from collections import Counter

def draw_cards(deck, n):
    return random.sample(deck, n)

def analyze_structure(cards, lang):
    types = [c["type"][lang] for c in cards]
    dominant = Counter(types).most_common(1)[0][0]

    if lang == "en":
        return f"Dominant theme: {dominant}."
    return f"ธีมหลักคือ {dominant}"
