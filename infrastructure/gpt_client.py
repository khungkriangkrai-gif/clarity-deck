from domain.models import DecisionContext

class GPTClient:
    def analyze(self, context: DecisionContext, cards: list):

        card_names = ", ".join([card.name for card in cards])

        # simple rule-based synthesis
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
The cards suggest that clarity will emerge through deliberate action.
Your fear appears to be tied to uncertainty rather than actual constraint.
Focus on structured decision-making and incremental progress.

Recommended Action:
1. Break the goal into 3 concrete steps.
2. Identify the worst-case scenario realistically.
3. Act despite incomplete information.
"""

        return insight.strip()
