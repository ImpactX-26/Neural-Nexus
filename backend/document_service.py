from pathlib import Path
from datetime import datetime

from backend.applicant_state import add_document
from backend.document_verification import verify_document


def extract_pdf_text(file_path):

    try:

        from PyPDF2 import PdfReader

        reader = PdfReader(str(file_path))

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text.strip()

    except Exception as error:

        return f"PDF extraction failed: {error}"


def extract_text_file(file_path):

    try:

        return Path(file_path).read_text(
            encoding="utf-8",
            errors="ignore"
        )

    except Exception as error:

        return f"Text extraction failed: {error}"


def extract_document_text(file_path):

    extension = file_path.suffix.lower()

    if extension == ".pdf":
        return extract_pdf_text(file_path)

    if extension == ".txt":
        return extract_text_file(file_path)

    return ""


def process_document(
    file_path,
    original_filename
):

    text = extract_document_text(file_path)

    verification = verify_document(
        filename=original_filename,
        extracted_text=text
    )

    document = {
        "filename": original_filename,
        "path": str(file_path),
        "type": file_path.suffix.lower(),
        "uploaded_at": datetime.utcnow().isoformat(),
        "text_length": len(text),
        "extracted_text": text[:15000],
        "verification": verification
    }

    add_document(document)

    return document