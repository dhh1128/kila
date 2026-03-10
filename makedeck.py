#!/usr/bin/env python3
import argparse
import re
import genanki
from pathlib import Path

def parse_markdown_table(md_text: str):
    """
    Parses a markdown table with header:
    lemma | tags | definition | notes
    """
    lines = [line.strip() for line in md_text.splitlines() if line.strip()]
    notes = []
    # find header line
    header_idx = None
    for i, line in enumerate(lines):
        if re.match(r'^lemma\s*\|\s*tags\s*\|\s*definition\s*\|\s*notes', line, re.I):
            header_idx = i
            break
    if header_idx is None or header_idx + 1 >= len(lines):
        raise ValueError("Markdown table header not found")

    # skip separator line
    for line in lines[header_idx + 2:]:
        cols = [c.strip() for c in line.split("|")]
        if len(cols) < 4:
            # pad missing columns
            cols += [""] * (4 - len(cols))
        lemma, tags_col, definition, notes_col = cols[:4]

        # Format the lemma with cloze syntax here
        cloze_lemma = f"{{{{c1::{lemma}}}}}"

        notes.append({
            "lemma": cloze_lemma,
            "definition": definition,
            "notes": notes_col,
            "tags": tags_col,
        })
        
    return notes


note_model = genanki.Model(
    1091735104,
    "Type-in", #"Cloze + Type-in",
    fields=[
        {"name": "Lemma"},
        {"name": "Definition"},
        {"name": "Notes"},
        {"name": "Tags"},
    ],
    templates=[
        # Cloze (passive recall) card
        #{
        #    "name": "Cloze Card",
        #    "qfmt": "Definition: {{Definition}}<br>Notes: {{Notes}}<br>Tags: {{Tags}}<br>{{cloze:Lemma}}",
        #    "afmt": "{{cloze:Lemma}}<br><br>{{Definition}}",
        #},
        # Type-in-the-answer card
        {
            "name": "Type-in Card",
            "qfmt": "Definition: {{Definition}}<br>Notes: {{Notes}}<br>Tags: {{Tags}}<br>Lemma: {{type:Lemma}}",
            "afmt": "{{Lemma}}",
        }
    ],
    model_type=genanki.Model.CLOZE,
)

def make_apkg(notes, output_file="output.apkg"):
    deck = genanki.Deck(
        2059400110,  # fixed unique deck ID
        "kila",
    )

    tag_split_pat = re.compile(r'[\s,]+')
    for n in notes:
        tags = [t for t in tag_split_pat.split(n["tags"]) if t]
        note = genanki.Note(
                model=note_model,
                fields=[
                    n["lemma"],         # Lemma
                    n["definition"],    # Definition
                    n["notes"],         # Notes
                    " ".join(tags),     # Tags
                ],
                sort_field=n["lemma"],
                tags=tags
            )

        deck.add_note(note)

    pkg = genanki.Package(deck)
    pkg.write_to_file(output_file)


def main():
    parser = argparse.ArgumentParser(description="Export Markdown glossary to Anki .apkg")
    parser.add_argument("input", type=Path, help="Input markdown file")
    parser.add_argument("output", type=Path, help="Output .apkg file")
    args = parser.parse_args()

    md_text = args.input.read_text(encoding="utf-8")
    notes = parse_markdown_table(md_text)
    make_apkg(notes, output_file=str(args.output))


if __name__ == "__main__":
    main()
