#!/usr/bin/env python3
"""
Parse QA_ARCHITECTURE_FROM_KB.md and print Python code for TOPICS (content_script.py).
Run from project root: python scripts/build_content_from_architecture.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARCH = ROOT / "QA_ARCHITECTURE_FROM_KB.md"


def parse_block(block: str) -> dict | None:
    lines = block.strip().split("\n")
    if not lines:
        return None
    # topic_id: xxx
    m = re.match(r"^## topic_id:\s*(\S+)", lines[0])
    if not m:
        return None
    topic_id = m.group(1).strip()
    data = {"topic_id": topic_id, "display_label": "", "suggested_questions": [], "next_suggested_topics": [], "answer": "", "citations": []}
    i = 1
    while i < len(lines):
        line = lines[i]
        if line.startswith("display_label:"):
            data["display_label"] = line.split(":", 1)[1].strip().strip('"')
            i += 1
        elif line.strip() == "suggested_questions:":
            i += 1
            while i < len(lines) and lines[i].startswith("  - "):
                data["suggested_questions"].append(lines[i][4:].strip().strip('"'))
                i += 1
        elif "next_suggested_topics" in line and line.strip().startswith("next_suggested_topics:"):
            rest = line.split(":", 1)[1].strip()
            if rest.startswith("["):
                inner = re.search(r"\[(.*?)\]", rest, re.DOTALL)
                if inner:
                    data["next_suggested_topics"] = [x.strip() for x in inner.group(1).split(",") if x.strip()]
            i += 1
            while i < len(lines):
                L = lines[i]
                if L.strip().startswith("- "):
                    data["next_suggested_topics"].append(L.strip()[2:].strip())
                    i += 1
                elif L.strip().startswith("answer:") or L.strip().startswith("citations:"):
                    break
                elif L.strip() == "":
                    i += 1
                else:
                    break
        elif line.strip() == "answer: |":
            i += 1
            answer_lines = []
            while i < len(lines) and not lines[i].strip().startswith("citations:"):
                answer_lines.append(lines[i])
                i += 1
            data["answer"] = "\n".join(answer_lines).strip()
            # Normalize: leading space on each line from the doc
            data["answer"] = re.sub(r"\n  ", "\n", data["answer"])
        elif line.strip().startswith("citations:"):
            i += 1
            while i < len(lines):
                L = lines[i]
                if L.strip().startswith("- "):
                    cit = L.strip()[2:].strip().strip('"')
                    if not cit.startswith(">"):  # skip note lines
                        data["citations"].append(cit)
                elif L.strip().startswith(">"):
                    pass  # skip note
                elif re.match(r"^## topic_id:", L) or (L.strip() == "---" and i + 1 < len(lines) and "topic_id" in lines[i + 1]):
                    break
                elif L.strip() and not L.strip().startswith("-"):
                    break
                i += 1
        else:
            i += 1
    return data if data["display_label"] and data["answer"] else None


def main():
    text = ARCH.read_text(encoding="utf-8")
    # Split so each block starts with "## topic_id: xxx"
    parts = re.split(r"\n(?=## topic_id: )", text)
    topics = []
    for block in parts:
        if not block.strip().startswith("## topic_id: "):
            continue
        d = parse_block(block)
        if d:
            topics.append(d)
    # Output Python
    print("# Auto-generated from QA_ARCHITECTURE_FROM_KB.md - do not edit by hand; re-run scripts/build_content_from_architecture.py")
    print("from __future__ import annotations")
    print("from dataclasses import dataclass")
    print("from typing import Optional")
    print()
    print("@dataclass")
    print("class Topic:")
    print("    id: str")
    print("    label: str")
    print("    answer: str")
    print("    citations: list[str]")
    print("    suggested_questions: list[str]")
    print("    next_suggested_topics: list[str]")
    print()
    print("TOPICS: list[Topic] = [")
    for d in topics:
        qs = repr(d["suggested_questions"])
        next_ids = repr(d["next_suggested_topics"])
        ans = repr(d["answer"])  # safe escaping for any quotes/newlines
        cit = repr(d["citations"])
        print(f'    Topic(')
        print(f'        id="{d["topic_id"]}",')
        print(f'        label={repr(d["display_label"])},')
        print(f'        answer={ans},')
        print(f'        citations={cit},')
        print(f'        suggested_questions={qs},')
        print(f'        next_suggested_topics={next_ids},')
        print(f'    ),')
    print("]")
    print()
    print("DEFAULT_WELCOME_TOPIC_IDS = [\"what_is_hsa\", \"young_adults\", \"triple_tax\", \"misconceptions\", \"qualified_expenses\"]")
    print("SUGGESTED_TOPIC_LABELS = [t.label for t in TOPICS]")
    print()
    print("def get_topic_by_id(topic_id: str) -> Optional[Topic]:")
    print("    for t in TOPICS:")
    print("        if t.id == topic_id:")
    print("            return t")
    print("    return None")
    print()
    print("def get_topic_by_label(label: str) -> Optional[Topic]:")
    print("    label_clean = label.strip()")
    print("    for t in TOPICS:")
    print("        if t.label.strip() == label_clean:")
    print("            return t")
    print("    return None")
    print()
    print("def get_topic_by_suggested_question(user_message: str) -> Optional[Topic]:")
    print("    msg = user_message.strip().lower()")
    print("    if not msg:")
    print("        return None")
    print("    for t in TOPICS:")
    print("        for q in t.suggested_questions:")
    print("            if q.strip().lower() == msg:")
    print("                return t")
    print("            if q.strip().lower() in msg or msg in q.strip().lower():")
    print("                return t")
    print("    return None")
    print()
    print("def get_all_topics() -> list[Topic]:")
    print("    return list(TOPICS)")
    print()
    print("def get_welcome_topics() -> list[Topic]:")
    print("    return [t for t in TOPICS if t.id in DEFAULT_WELCOME_TOPIC_IDS]")


if __name__ == "__main__":
    main()
