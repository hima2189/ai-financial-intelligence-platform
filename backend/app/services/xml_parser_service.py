from pathlib import Path
import xml.etree.ElementTree as ET


def extract_text_from_xml(file_path: Path) -> str:
    """
    Extract text content from all XML elements.
    """

    tree = ET.parse(file_path)

    root = tree.getroot()

    extracted_text = []

    for element in root.iter():

        if element.text:

            cleaned_text = element.text.strip()

            if cleaned_text:
                extracted_text.append(cleaned_text)

    return " ".join(extracted_text)