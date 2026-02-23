from openai import OpenAI

class GPTClient:

    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

        self.system_prompt = """
You are the Clarity Deck Intelligence.

You do not predict the future.
You reveal structural truth.

You analyze psychological patterns, decision tension, and energetic direction.

Tone: precise, grounded, strategic.
No mysticism. No destiny claims.

Clarity over comfort.
Precision over poetry.
"""

    def analyze(self, context, cards):

        card_block = "\n".join(
            [f"{c['title']}: {c['description']}" for c in cards]
        )

        user_prompt = f"""
USER CONTEXT:
{context}

DRAWN CARDS:
{card_block}

Follow Clarity Deck Protocol.
Use required structure:
CORE FORCE
WHAT YOU’RE AVOIDING
STRUCTURAL TRUTH
CLARITY SHIFT

Do not predict.
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
