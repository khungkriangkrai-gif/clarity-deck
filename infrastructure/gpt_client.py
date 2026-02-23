from openai import OpenAI

class GPTInsightClient:

    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def analyze(self, context, cards):

        card_text = "\n".join(
            [f"{c.name} - Archetype: {c.archetype} - Meaning: {c.meaning}" for c in cards]
        )

        prompt = f"""
You are a strategic decision intelligence system.

Decision Context:
Topic: {context.topic}
Situation: {context.situation}
Goal: {context.goal}
Fear: {context.fear}

Cards Drawn:
{card_text}

Provide:
1. Structural Analysis
2. Psychological Insight
3. Hidden Tension
4. Strategic Recommendation
5. Concrete Next Action

Be clear and decisive.
"""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

        return response.choices[0].message.content
