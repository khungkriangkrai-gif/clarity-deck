import os
from openai import OpenAI


class GPTClient:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found")

        self.client = OpenAI(api_key=api_key)

    def analyze(self, context: str, cards: list[dict]) -> str:
        card_text = "\n".join(
            f"- {c['title']}: {c['description']}"
            for c in cards
        )

        prompt = f"""
You are a strategic AI advisor.

Decision Context:
{context}

Available Cards:
{card_text}

Provide a structured strategic insight.
"""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a strategic decision intelligence engine."},
                {"role": "user", "content": prompt},
            ],
        )

        return response.choices[0].message.content
