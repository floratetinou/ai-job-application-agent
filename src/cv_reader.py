
from pathlib import Path
from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    """Extrahiert Text aus einem PDF-Lebenslauf."""

    pdf_file = Path(pdf_path)

    if not pdf_file.exists():
        raise FileNotFoundError(
            f"Die PDF-Datei wurde nicht gefunden: {pdf_file}"
        )

    reader = PdfReader(str(pdf_file))
    pages_text = []

    for page in reader.pages:
        text = page.extract_text() or ""
        pages_text.append(text)

    cv_text = "\n".join(pages_text).strip()

    if not cv_text:
        raise ValueError(
            "Kein Text gefunden. "
            "Das PDF ist möglicherweise ein Scan."
        )

    return cv_text
