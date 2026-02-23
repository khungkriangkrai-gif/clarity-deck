from domain.models import DecisionContext


class GPTClient:

    def analyze(self, context: DecisionContext, cards):

        # รองรับหลายรูปแบบ input
        if hasattr(cards, "cards"):
            cards = cards.cards

        card_names_list = []

        for c in cards:
            if hasattr(c, "name"):
                card_names_list.append(c.name)
            else:
                card_names_list.append(str(c))

        card_names = ", ".join(card_names_list)

        insight = f"""
Strategic Insight (Prototype Mode)

Topic: {context.topic}

Cards Drawn: {card_names}

Current Situation:
{context.situation}

Desired Goal:
{context.goal}

Main Fear:
{context.fear}

Interpretation:
The cards suggest that clarity will come from decisive action.
Your fear appears to be driven more by uncertainty than real limitation.

Recommended Action:
1. Define one concrete next move.
2. Reduce ambiguity with data.
3. Act before confidence is perfect.
"""

        return insight.strip()
