from pathlib import Path

from docling.document_converter import DocumentConverter
from rich import print as rprint


def parse_document_with_docling(path: str):
    file_path = Path(path)

    if not file_path.exists():
        raise ValueError("Invalid file path")

    if not file_path.is_file():
        raise ValueError(f"Path is not a file: {path}")

    converter = DocumentConverter()

    doc = converter.convert(path).document

    rprint(doc.export_to_dict())
