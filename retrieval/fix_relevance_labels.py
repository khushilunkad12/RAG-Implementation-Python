import csv
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

EVALUATION_FILE = os.path.join(
    BASE_DIR,
    "retrieval_evaluation.csv"
)


# ============================================================
# Verified relevance rules
# ============================================================
#
# Relevance is determined by the CONTENT of the retrieved
# chunk, not by its rank.
#
# 1 = chunk directly helps answer the question
# 0 = chunk does not directly help answer the question
#
# We identify chunks using their source + chunk_id.
# ============================================================

RELEVANT_CHUNKS = {

    # --------------------------------------------------------
    # Python
    # --------------------------------------------------------

    "What is Python used for?": {
        ("python.txt", "3"),
        ("python.txt", "python.txt_3"),
    },


    # --------------------------------------------------------
    # RAG
    # --------------------------------------------------------

    "What is retrieval augmented generation?": {
        ("rag.txt", "0"),
        ("rag.txt", "rag.txt_0"),
    },


    # --------------------------------------------------------
    # Database
    # --------------------------------------------------------

    "What is a database?": {
        ("databases.txt", "0"),
        ("databases.txt", "databases.txt_0"),
    },


    # --------------------------------------------------------
    # Machine Learning
    # --------------------------------------------------------

    "What is machine learning?": {
        ("machine_learning.txt", "0"),
        ("machine_learning.txt", "machine_learning.txt_0"),
    },


    # --------------------------------------------------------
    # Software Testing
    # --------------------------------------------------------

    "What is software testing?": {
        ("software_testing.txt", "0"),
        ("software_testing.txt", "software_testing.txt_0"),
    },
}


# ============================================================
# Load CSV
# ============================================================

with open(
    EVALUATION_FILE,
    "r",
    encoding="utf-8",
    newline=""
) as file:

    reader = csv.DictReader(file)

    rows = list(reader)
    fieldnames = reader.fieldnames


# ============================================================
# Apply verified labels
# ============================================================

corrected = 0

for row in rows:

    question = row["question"]
    source = row["source"]
    chunk_id = row["chunk_id"]

    key = (source, chunk_id)

    new_relevance = 1 if (
        question in RELEVANT_CHUNKS
        and key in RELEVANT_CHUNKS[question]
    ) else 0

    old_relevance = int(row["relevance"])

    if old_relevance != new_relevance:

        row["relevance"] = str(new_relevance)

        corrected += 1

        print(
            f"Corrected: "
            f"{question} | "
            f"{row['strategy']} | "
            f"Rank {row['rank']} | "
            f"{old_relevance} -> {new_relevance}"
        )


# ============================================================
# Save corrected CSV
# ============================================================

with open(
    EVALUATION_FILE,
    "w",
    encoding="utf-8",
    newline=""
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(rows)


print()
print("=" * 70)
print("RELEVANCE LABEL CORRECTION COMPLETED")
print("=" * 70)

print(
    f"Corrections applied: {corrected}"
)

print(
    f"Updated file: {EVALUATION_FILE}"
)