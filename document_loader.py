import os

DOCUMENT_FOLDER = "documents"


def load_documents():

    documents = []

    if not os.path.exists(DOCUMENT_FOLDER):
        raise FileNotFoundError(
            f"{DOCUMENT_FOLDER} folder not found."
        )

    for filename in os.listdir(DOCUMENT_FOLDER):

        if filename.endswith(".txt"):

            filepath = os.path.join(
                DOCUMENT_FOLDER,
                filename
            )

            with open(
                filepath,
                "r",
                encoding="utf-8"
            ) as file:

                text = file.read()

            documents.append(
                {
                    "filename": filename,
                    "text": text
                }
            )

    return documents