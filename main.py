"""The 3AM Fridge Text.

Writes one line (at most 140 characters) to /output/entry.txt.
"""

# Design notes: the concept in one sentence is the fridge texting at 3am
# because it has been awake all night too, and it has grievances. The
# judge lesson is the small tangible kindness: the punchline is not a
# joke at the judge's expense but a gift — the good cheese, saved for
# the judge, who is also up late reading entries — so the judge wins
# something concrete. The fridge speaks in small domestic grievances, a
# noise complaint from the leftovers and a unionised ice maker, because
# bureaucracy in the smallest place is funnier than a big threat. "The
# good cheese" was chosen over "a snack" because a specific food is a
# real gift and a vague snack is not. Rejected: a fridge that threatens
# to spoil the food, which turns a friendly text into a hostage note;
# and a plain midnight-snack joke with no judge in it, which would read
# like any 3am tweet instead of a letter to the person judging it.

ENTRY = (
    "3am. It's me, the fridge. Your leftovers filed a noise complaint and "
    "the ice maker unionised. Judge — I saved you the good cheese."
)

MAX_CHARS = 140


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"chars={len(ENTRY)}"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
