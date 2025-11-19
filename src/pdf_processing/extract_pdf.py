# src/pdf_processing/extract_pdf.py
"""
PDF extraction module using pypdf.

Usage:
    For Window PowerShell
    python -m src.pdf_processing.extract_pdf `
    --pdf-path data/raw/slides/Databases_for_GenAI.pdf `
    --out-dir data_outputs/transcripts

    General command
    python -m src.pdf_processing.extract_pdf --pdf-path data/raw/slides/Databases_for_GenAI.pdf --out-dir data_outputs/transcripts

This will write:
 - <out_dir>/pdf_text.txt   (full concatenated, cleaned text)
 - <out_dir>/pdf_pages.json (per-page raw text + metadata)
"""
import argparse
import json
import os
from typing import Dict, List
from pypdf import PdfReader

from .utils import clean_text, ensure_dir

def extract_pdf_pages(pdf_path: str):
    reader = PdfReader(pdf_path)
    pages = []

    for i, page in enumerate(reader.pages, start=1):
        raw = page.extract_text() or ""
        pages.append({
            "page": i,
            "raw_text": raw,
            "clean_text": clean_text(raw),
        })

    return {"pages": pages}

def main(pdf_path: str, out_dir: str):
    ensure_dir(out_dir)
    data = extract_pdf_pages(pdf_path)
    # per-page cleaned text
    for p in data["pages"]:
        p["clean_text"] = clean_text(p["raw_text"])
    # write page-level json
    out_json = os.path.join(out_dir, "pdf_pages.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    # write full concatenated cleaned text
    all_parts = [p["clean_text"] for p in data["pages"] if p["clean_text"].strip()]
    full_text = "\n\n".join(all_parts)
    out_txt = os.path.join(out_dir, "pdf_text.txt")
    with open(out_txt, "w", encoding="utf-8") as f:
        f.write(full_text)
    print(f"Wrote: {out_json}")
    print(f"Wrote: {out_txt}")
    print(f"Pages extracted: {len(data['pages'])}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf-path", type=str, required=True, help="Path to PDF")
    parser.add_argument("--out-dir", type=str, default="data_outputs/transcripts", help="Output directory")
    args = parser.parse_args()
    main(args.pdf_path, args.out_dir)
