from infrastructure.deck_repository import DeckRepository
from infrastructure.gpt_client import GPTClient
from application.run_reading_usecase import RunReadingUseCase

deck_repo = DeckRepository()
gpt_client = GPTClient(api_key="YOUR_KEY")

usecase = RunReadingUseCase(deck_repo, gpt_client)

reading, analysis = usecase.execute(
    context="ฉันควรเปลี่ยนงานไหม",
    num_cards=1
)

print(analysis)
