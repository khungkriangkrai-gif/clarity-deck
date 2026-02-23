from domain.models import ReadingResult
from domain.tarot_engine import TarotEngine
from domain.models import Reading

class RunReadingUseCase:

    def __init__(self, deck_repository, gpt_client):
        self.deck_repository = deck_repository
        self.gpt_client = gpt_client

    def execute(self, context, num_cards):

        deck = self.deck_repository.load_deck()

        import random
        cards = random.sample(deck, num_cards)

        analysis = self.gpt_client.analyze(context, cards)

        return ReadingResult(cards=cards, analysis=analysis)
