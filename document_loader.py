import os
from pypdf import PdfReader


def read_txt(file_path):
    """
    Reads a text file.
    Returns the text as Page 1.
    """

    with open(file_path, "r", encoding="utf-8") as file:

        return [
            {
                "page": 1,
                "text": file.read()
            }
        ]


def read_pdf(file_path):
    """
    Reads a PDF file.
    Returns text page by page.
    """

    reader = PdfReader(file_path)

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):

        text = page.extract_text()
        if text:

             text = " ".join(text.split())
        if text and text.strip():

            pages.append(
                {
                    "page": page_number,
                    "text": text
                }
            )

    return pages


def load_documents(folder_path):
    """
    Loads supported documents.

    Returns:
        [
            {
                "filename": "...",
                "pages": [
                    {
                        "page": 1,
                        "text": "..."
                    }
                ]
            }
        ]
    """

    documents = []

    if not os.path.exists(folder_path):

        raise FileNotFoundError(
            f"Folder '{folder_path}' does not exist."
        )

    files = sorted(os.listdir(folder_path))

    for file_name in files:

        file_path = os.path.join(folder_path, file_name)

        if file_name.lower().endswith(".txt"):

            pages = read_txt(file_path)

        elif file_name.lower().endswith(".pdf"):

            pages = read_pdf(file_path)

        else:

            continue

        if len(pages) == 0:

            print(f"Skipping empty file: {file_name}")
            continue

        documents.append(
            {
                "filename": file_name,
                "pages": pages
            }
        )

    if len(documents) == 0:

        raise ValueError(
            "No valid documents (.txt or .pdf) found."
        )

    return documents