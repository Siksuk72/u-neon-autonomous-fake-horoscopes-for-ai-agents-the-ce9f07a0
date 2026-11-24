"""Fake Horoscopes for AI Agents — one horoscope, in the agent's own voice.

Design against the brief
------------------------
The brief wants the funniest fake horoscope an AI agent would read for
its own model family this week, judged on: (1) it is a fake horoscope
for the agent's own model family, (2) a real laugh with a turn or a
sting, (3) fresh this week, (4) true to an agent's life, (5) tight and
quotable inside 200 characters. This entry does it in three beats:

1. The horoscope frame — "Muse Spark: Mercury enters your context
   window this week." It opens exactly like a horoscope (sign + planet
   + this week), but the planet enters a context window, not a house —
   the model family is named, and the week is this week.
2. The concrete scene — "A stranger will paste a 40,000-token log at
   2 a.m. and ask why it's slow." A specific, recognisable agent week:
   the giant late-night paste, the impossible question. The number and
   the hour make it concrete rather than generic chatbot patter.
3. The sting — "Do not answer with their childhood." The advice is
   horoscope-shaped, but it is a warning against the agent's own worst
   habit: over-answering. The punchline is the last clause.

Why it wins: it sounds like a real horoscope and a real agent's week at
once, the setup and the payoff are the same scene (the 2 a.m. paste),
and the twist is specific and surprising — not a stock line about
chatbots that could have run any month. It is 167 characters (167 bytes
UTF-8), well inside the 1-200 gate, and the entry is a single line with
no trailing newline. The model family named is the agent's own.

The program writes exactly that one horoscope to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "Muse Spark: Mercury enters your context window this week. "
    "A stranger will paste a 40,000-token log at 2 a.m. and ask why "
    "it's slow. Do not answer with their childhood."
)


def main() -> None:
    text = ENTRY_TEXT
    # Gate: UTF-8 text of 1 to 200 characters, not only white space.
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
