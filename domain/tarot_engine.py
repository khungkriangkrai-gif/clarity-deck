import random
from .models import Card

class TarotEngine:

    def draw(self, deck: list[Card], n: int) -> list[Card]:
        return random.sample(deck, n)
