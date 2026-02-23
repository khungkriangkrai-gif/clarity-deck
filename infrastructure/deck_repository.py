from typing import List, Dict


class DeckRepository:
    def __init__(self):
        # mock data (แทน database ชั่วคราว)
        self._decks = [
            {
                "id": 1,
                "title": "Strategic Clarity Framework",
                "description": "Core strategic decision deck"
            },
            {
                "id": 2,
                "title": "Governance Activation Model",
                "description": "Execution governance structure"
            }
        ]

    def get_all(self) -> List[Dict]:
        return self._decks

    def get_by_id(self, deck_id: int) -> Dict | None:
        for deck in self._decks:
            if deck["id"] == deck_id:
                return deck
        return None
