class RunReadingUseCase:

    def __init__(self, deck_repo, gpt_client):
        self.deck_repo = deck_repo
        self.engine = TarotEngine()
        self.gpt = gpt_client

    def execute(self, context, num_cards):

        deck = self.deck_repo.load_deck()
        cards = self.engine.draw(deck, num_cards)

        reading = Reading(context=context, cards=cards)

        ai_analysis = self.gpt.analyze(context, cards)

        return reading, ai_analysis
