import os
import json
from src.pdf_processing.extract_pdf import extract_pdf_pages, main


def test_pdf_exists(pdf_path):
    assert os.path.exists(pdf_path), "PDF file does not exist!"


def test_extract_returns_pages(pdf_path):
    data = extract_pdf_pages(pdf_path)
    assert "pages" in data
    assert len(data["pages"]) > 0, "No pages extracted from PDF."


def test_page_has_raw_text(pdf_path):
    data = extract_pdf_pages(pdf_path)
    first_page = data["pages"][0]
    assert "raw_text" in first_page
    assert isinstance(first_page["raw_text"], str)
    assert len(first_page["raw_text"]) > 0, "Empty raw text on page 1."


def test_main_writes_output(pdf_path, test_output_dir):
    main(pdf_path, str(test_output_dir))

    json_path = test_output_dir / "pdf_pages.json"
    txt_path = test_output_dir / "pdf_text.txt"

    assert json_path.exists(), "pdf_pages.json not created!"
    assert txt_path.exists(), "pdf_text.txt not created!"

    # Validate JSON format
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "pages" in data
    assert len(data["pages"]) > 0


def test_cleaned_text_is_not_empty(pdf_path):
    data = extract_pdf_pages(pdf_path)
    cleaned = [p["clean_text"] for p in data["pages"] if p["clean_text"].strip()]
    assert len(cleaned) > 0, "No cleaned text extracted."
