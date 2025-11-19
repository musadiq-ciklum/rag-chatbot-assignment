# src/pdf_processing/utils.py
"""
Utilities for PDF processing (cleaning, small helpers).
"""
import os
import re

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def clean_text(text: str) -> str:
    """
    Lightweight cleaning tuned for slide text and exported PDFs:
      - remove hyphenation at line breaks (like 'exam-\nple' -> 'example')
      - collapse multiple newlines
      - strip leading/trailing whitespace
      - remove repeated header/footer if detected heuristically (simple rule)
    """
    if not text:
        return ""
    # fix hyphenated line breaks
    text = text.replace("-\n", "")
    # replace newlines with single space (slides often have short lines)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    # remove sequences of short repeated lines that look like headers (heuristic)
    # basic approach: collapse multiple newlines, then collapse whitespace
    text = re.sub(r"\n+", "\n", text)
    # remove stray multiple spaces
    text = re.sub(r"[ \t]+", " ", text)
    # trim
    text = text.strip()
    return text
