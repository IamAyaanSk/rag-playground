from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


def load_pdf(path: str):
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    if not file_path.is_file():
        raise ValueError(f"Path is not a file: {path}")

    if file_path.suffix.lower() != ".pdf":
        raise ValueError(f"Expected a PDF file: {path}")

    try:
        pdf_loader = PyPDFLoader(path)
        documents = pdf_loader.load()

        if not documents:
            raise ValueError(f"No content extracted from PDF: {path}")

        return documents

    except Exception as e:
        raise RuntimeError(f"Failed to load PDF '{path}': {e}") from e
