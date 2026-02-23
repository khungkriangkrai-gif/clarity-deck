from dataclasses import dataclass
from typing import List

@dataclass
class DecisionContext:
    topic: str
    situation: str
    goal: str
    fear: str

@dataclass
class Card:
    name: str
    archetype: str
    meaning: str

@dataclass
class Reading:
    context: DecisionContext
    cards: List[Card]
