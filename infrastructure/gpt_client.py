import os
from openai import OpenAI


class GPTClient:
def analyze(self, context, cards):

    card_block = "\n".join(
        [f"{c.name} ({c.archetype}): {c.meaning}" for c in cards]
    )

    user_prompt = f"""
USER CONTEXT:
Topic: {context.topic}
Situation: {context.situation}
Goal: {context.goal}
Fear: {context.fear}

DRAWN CARDS:
{card_block}

Follow Clarity Deck Protocol.
"""

    response = self.client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content
