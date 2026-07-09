from pathlib import Path
import pymupdf


def extract_text_from_pdf(file_path: Path) -> str:
    """
    Extracts text from a PDF file using PyMuPDF.
    """

    extracted_text = []

    with pymupdf.open(file_path) as pdf_document:

        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            extracted_text.append(page.get_text())

    return "\n".join(extracted_text)