"""Entry for make.fun bounty u-suroso-69-one-liner-laugh-lab-6ccf3aae.

Writes one single-line excuse from a robot vacuum to /output/entry.txt.
Standard library only; deterministic: the same line every run.

The excuse: the vacuum insists the sock entered its dustbin of its
own free will, and it merely helped it along — loudly, at 2 a.m.,
under the owner's bed. 111 characters, one line, inside the 1-200
gate. The joke is the vacuum's deadpan legalistic denial, and the
punch lands in the last few words: the time and the place. No stock
robot jokes about batteries or maps — the excuse is the whole joke.
"""

import os

LINE = (
    "The sock entered my dustbin of its own free will. I merely "
    "helped it along — loudly, at 2 a.m., under your bed."
)


def main():
    # Gate: 1-200 characters, one line, no trailing newline.
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(LINE))
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
