import os
import csv
from collections import defaultdict


# ==========================================
# Paths
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

INPUT_FILE = os.path.join(
    BASE_DIR,
    "chunking_comparison_results.csv"
)

OUTPUT_FILE = os.path.join(
    BASE_DIR,
    "retrieval_evaluation.csv"
)


# ==========================================
# Load Comparison Results
# ==========================================

def load_results():

    rows = []

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            rows.append(row)

    return rows


# ==========================================
# Calculate Precision@3
# ==========================================

def precision_at_3(relevance_labels):

    if not relevance_labels:
        return 0.0

    relevant = sum(relevance_labels)

    return relevant / len(relevance_labels)


# ==========================================
# Calculate MRR
# ==========================================

def calculate_mrr(relevance_labels):

    for rank, label in enumerate(
        relevance_labels,
        start=1
    ):

        if label == 1:
            return 1 / rank

    return 0.0


# ==========================================
# Main Evaluation
# ==========================================

def main():

    print("=" * 70)
    print("RETRIEVAL QUALITY EVALUATION")
    print("=" * 70)

    rows = load_results()

    grouped = defaultdict(list)

    # Group by question + strategy
    for row in rows:

        key = (
            row["question"],
            row["strategy"]
        )

        grouped[key].append(row)

    evaluation_rows = []

    # ======================================
    # Manual Relevance Evaluation
    # ======================================

    for (question, strategy), results in grouped.items():

        # Sort by rank
        results.sort(
            key=lambda x: int(x["rank"])
        )

        print("\n")
        print("=" * 70)
        print(f"QUESTION: {question}")
        print(f"STRATEGY: {strategy}")
        print("=" * 70)

        relevance_labels = []

        for result in results:

            rank = int(result["rank"])

            print("\n")
            print(f"Rank: {rank}")
            print(f"Score: {result['score']}")
            print(f"Source: {result['source']}")
            print(f"Chunk ID: {result['chunk_id']}")

            print("\nText:")
            print(result["text_preview"])

            print("\nIs this chunk relevant?")
            print("Enter 1 = Relevant")
            print("Enter 0 = Not relevant")

            while True:

                label = input(
                    "Relevance (0/1): "
                ).strip()

                if label in ["0", "1"]:
                    break

                print(
                    "Please enter only 0 or 1."
                )

            relevance = int(label)

            relevance_labels.append(
                relevance
            )

            evaluation_rows.append({
                "question": question,
                "strategy": strategy,
                "rank": rank,
                "score": result["score"],
                "source": result["source"],
                "chunk_id": result["chunk_id"],
                "relevance": relevance,
                "text_preview": result["text_preview"]
            })

        # ==================================
        # Metrics
        # ==================================

        precision = precision_at_3(
            relevance_labels
        )

        mrr = calculate_mrr(
            relevance_labels
        )

        print("\n")
        print("--- Metrics ---")

        print(
            f"Precision@3: {precision:.2f}"
        )

        print(
            f"MRR: {mrr:.2f}"
        )

    # ======================================
    # Save Evaluation Results
    # ======================================

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        fieldnames = [
            "question",
            "strategy",
            "rank",
            "score",
            "source",
            "chunk_id",
            "relevance",
            "text_preview"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(
            evaluation_rows
        )

    print("\n")
    print("=" * 70)
    print("EVALUATION COMPLETED")
    print("=" * 70)

    print(
        f"Saved to: {OUTPUT_FILE}"
    )

    print(
        f"Total evaluated chunks: "
        f"{len(evaluation_rows)}"
    )


if __name__ == "__main__":
    main()