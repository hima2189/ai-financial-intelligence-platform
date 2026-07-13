from pathlib import Path

def extract_text_from_txt(file_path: Path) -> str:
    """
    Extracts text from a TXT file.
    """

    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()