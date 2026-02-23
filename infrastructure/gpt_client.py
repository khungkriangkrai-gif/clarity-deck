from domain.models import DecisionContext

class GPTClient:

    def analyze(self, context: DecisionContext, reading):

        # รองรับทั้ง list และ Reading object
        if hasattr(reading, "cards"):
            cards = reading.cards
        else:
            cards = reading

        card_names = ", ".join([c.name for c in cards])

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
The cards indicate that clarity will come from structured action.
Your fear is likely driven by uncertainty rather than real limitation.

Recommended Action:
1. Define the next concrete move.
2. Reduce ambiguity through data.
3. Act before confidence is perfect.
"""

        return insight.strip()
