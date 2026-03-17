#!/usr/bin/env python3

import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(ROOT, "README.md")


def to_title(name):
    """Convert folder or filename to human-readable title.
    '1_2_hobbies' -> '1.2 Hobbies'
    'Conversational' -> 'Conversational'
    """
    match = re.match(r'^(\d+)_(\d+)_(.+)$', name)
    if match:
        major, minor, rest = match.groups()
        label = rest.replace('_', ' ').title()
        return f"{major}.{minor} {label}"
    return name.replace('_', ' ').replace('-', ' ').title()


def generate_readme():
    topics = sorted(
        e for e in os.listdir(ROOT)
        if os.path.isdir(os.path.join(ROOT, e)) and not e.startswith('.')
    )

    if not topics:
        print("No topic folders found.")
        return

    lines = ["# German Study Guide", ""]

    for topic in topics:
        topic_dir = os.path.join(ROOT, topic)
        files = sorted(
            f for f in os.listdir(topic_dir)
            if f.endswith('.md') and os.path.isfile(os.path.join(topic_dir, f))
        )

        if not files:
            continue

        lines.append(f"## {to_title(topic)}")
        lines.append("")

        for filename in files:
            base = os.path.splitext(filename)[0]
            title = to_title(base)
            link = f"{topic}/{filename}"
            lines.append(f"- [{title}]({link})")

        lines.append("")

    content = "\n".join(lines)
    with open(OUTPUT, "w") as f:
        f.write(content)

    print(f"README.md written to {OUTPUT}")
    print(content)


if __name__ == "__main__":
    generate_readme()
