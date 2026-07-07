#!/usr/bin/env python3
"""
Script pentru parsarea PDF-urilor din `inbox/` folosind pdfplumber.
Output: Fișiere JSON cu textul și metadatele extrase.
"""

import os
import json
import pdfplumber
from pathlib import Path
from typing import Dict, List, Optional


# Configurare
INBOX_DIR = "inbox"
OUTPUT_DIR = "processed"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def extract_pdf_metadata(pdf_path: str) -> Dict:
    """Extrage metadatele unui PDF."""
    with pdfplumber.open(pdf_path) as pdf:
        metadata = pdf.metadata
        return {
            "title": metadata.get("title", Path(pdf_path).stem),
            "author": metadata.get("author", "Unknown"),
            "pages": len(pdf.pages),
        }


def extract_pdf_text(pdf_path: str) -> List[Dict]:
    """Extrage textul și poziționarea din fiecare pagină a PDF-ului."""
    pages_content = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if text:
                pages_content.append({
                    "page_number": page_num,
                    "text": text,
                    "words": page.extract_words(),  # Poziționare cuvinte
                })
    return pages_content


def save_extracted_data(pdf_name: str, metadata: Dict, pages: List[Dict]) -> str:
    """Salvează datele extrase într-un fișier JSON."""
    output_data = {
        "metadata": metadata,
        "pages": pages,
    }
    output_path = os.path.join(OUTPUT_DIR, f"{pdf_name}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    return output_path


def process_pdfs() -> None:
    """Procesează toate PDF-urile din `inbox/` (inclusiv subdirectoare) și salvează output-ul."""
    pdf_files = []
    for root, dirs, files in os.walk(INBOX_DIR):
        for f in files:
            if f.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, f))

    if not pdf_files:
        print(f"[WARNING] Nu există PDF-uri în directorul `{INBOX_DIR}`.")
        return

    for pdf_path in pdf_files:
        rel_path = os.path.relpath(pdf_path, INBOX_DIR)
        print(f"[INFO] Procesez: {rel_path}")
        try:
            metadata = extract_pdf_metadata(pdf_path)
            pages = extract_pdf_text(pdf_path)
            # Salvare cu nume care păstrează structura subdirectoarelor
            pdf_stem = Path(rel_path).with_suffix('').as_posix().replace('/', '_')
            output_path = save_extracted_data(pdf_stem, metadata, pages)
            print(f"[SUCCESS] Salvat: {output_path}")
        except Exception as e:
            print(f"[ERROR] Eroare la procesarea {rel_path}: {e}")


if __name__ == "__main__":
    process_pdfs()