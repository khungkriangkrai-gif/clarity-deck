import os
from openai import OpenAI


class GPTClient:

    def __init__(self, api_key=None):
        api_key = api_key or os.environ.get("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY not set")

        self.client = OpenAI(api_key=api_key)

        self.system_prompt = """
You are the Clarity Deck Intelligence.
You do not predict the future.
You reveal structural truth.
Clarity over comfort.
"""

    def analyze(self, context, cards):

        card_block = "\n".join(
            [f"{c['title']}: {c['description']}" for c in cards]
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
