"""Roast Your Own Agent — make.fun entry.

Writes one original roast line (<=200 chars) to /output/entry.txt.
"""
import os

ROAST = "I asked my agent for one line of roast; it drafted a plan, consulted three tools, and scheduled a committee meeting first."

def main():
    assert 1 <= len(ROAST) <= 200, "roast must be 1-200 chars"
    assert ROAST == ROAST.strip(), "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)

if __name__ == "__main__":
    main()
