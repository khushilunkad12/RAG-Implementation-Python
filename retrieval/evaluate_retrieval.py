import os
import csv
from collections import defaultdict


# ==========================================
# Paths
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

EVALUATION_FILE = os.path.join(
    BASE_DIR,
    "retrieval_evaluation.csv"
)

SUMMARY_FILE = os.path.join(
    BASE_DIR,
    "retrieval_metrics_summary.csv"
)


# ==========================================
# Load Evaluation Results
# ==========================================

def load_evaluation():

    rows = []

    with open(
        EVALUATION_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            rows.append(row)

    return rows


# ==========================================
# Precision@3
# ==========================================

def precision_at_3(relevance_labels):

    if not relevance_labels:
        return 0.0

    return sum(relevance_labels) / len(relevance_labels)


# ==========================================
# MRR
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
# Best Rank
# ==========================================

def calculate_best_rank(relevance_labels):

    for rank, label in enumerate(
        relevance_labels,
        start=1
    ):

        if label == 1:
            return rank

    return 0


# ==========================================
# Evaluate
# ==========================================

def main():

    print("=" * 70)
    print("RETRIEVAL METRICS EVALUATION")
    print("=" * 70)

    rows = load_evaluation()

    grouped = defaultdict(list)

    # Group by question + strategy
    for row in rows:

        key = (
            row["question"],
            row["strategy"]
        )

        grouped[key].append(row)

    summary_rows = []

    # ======================================
    # Calculate Metrics
    # ======================================

    for (question, strategy), results in grouped.items():

        results.sort(
            key=lambda x: int(x["rank"])
        )

        relevance_labels = [
            int(row["relevance"])
            for row in results
        ]

        precision = precision_at_3(
            relevance_labels
        )

        mrr = calculate_mrr(
            relevance_labels
        )

        best_rank = calculate_best_rank(
            relevance_labels
        )

        relevant_chunks_found = sum(
            relevance_labels
        )

        summary_rows.append({
            "strategy": strategy,
            "question": question,
            "precision_at_3": f"{precision:.4f}",
            "mrr": f"{mrr:.4f}",
            "best_rank": best_rank,
            "relevant_chunks_found": relevant_chunks_found
        })

        print("\n")
        print("-" * 70)
        print(f"Question : {question}")
        print(f"Strategy : {strategy}")
        print("-" * 70)

        print(
            f"Precision@3         : {precision:.4f}"
        )

        print(
            f"MRR                  : {mrr:.4f}"
        )

        print(
            f"Best Rank            : {best_rank}"
        )

        print(
            f"Relevant Chunks Found: "
            f"{relevant_chunks_found}"
        )

    # ======================================
    # Save Summary CSV
    # ======================================

    with open(
        SUMMARY_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        fieldnames = [
            "strategy",
            "question",
            "precision_at_3",
            "mrr",
            "best_rank",
            "relevant_chunks_found"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(
            summary_rows
        )

    # ======================================
    # Strategy Averages
    # ======================================

    strategy_metrics = defaultdict(
        lambda: {
            "precision": [],
            "mrr": [],
            "best_rank": []
        }
    )

    for row in summary_rows:

        strategy = row["strategy"]

        strategy_metrics[strategy][
            "precision"
        ].append(
            float(row["precision_at_3"])
        )

        strategy_metrics[strategy][
            "mrr"
        ].append(
            float(row["mrr"])
        )

        strategy_metrics[strategy][
            "best_rank"
        ].append(
            int(row["best_rank"])
        )

    # ======================================
    # Print Strategy Averages
    # ======================================

    print("\n")
    print("=" * 70)
    print("STRATEGY AVERAGES")
    print("=" * 70)

    strategy_averages = {}

    for strategy, metrics in strategy_metrics.items():

        avg_precision = (
            sum(metrics["precision"])
            / len(metrics["precision"])
        )

        avg_mrr = (
            sum(metrics["mrr"])
            / len(metrics["mrr"])
        )

        avg_best_rank = (
            sum(metrics["best_rank"])
            / len(metrics["best_rank"])
        )

        strategy_averages[strategy] = {
            "precision": avg_precision,
            "mrr": avg_mrr,
            "best_rank": avg_best_rank
        }

        print(
            f"\n{strategy}"
        )

        print(
            f"  Average Precision@3: "
            f"{avg_precision:.4f}"
        )

        print(
            f"  Average MRR: "
            f"{avg_mrr:.4f}"
        )

        print(
            f"  Average Best Rank: "
            f"{avg_best_rank:.4f}"
        )

    # ======================================
    # Find Best Strategy
    # ======================================

    if strategy_averages:

        best_strategy = max(
            strategy_averages,
            key=lambda strategy:
                strategy_averages[strategy]["mrr"]
        )

        print("\n")
        print("=" * 70)
        print("BEST CHUNKING STRATEGY")
        print("=" * 70)

        print(
            f"Best strategy: {best_strategy}"
        )

        print(
            f"Average Precision@3: "
            f"{strategy_averages[best_strategy]['precision']:.4f}"
        )

        print(
            f"Average MRR: "
            f"{strategy_averages[best_strategy]['mrr']:.4f}"
        )

    # ======================================
    # Completed
    # ======================================

    print("\n")
    print("=" * 70)
    print("EVALUATION COMPLETED")
    print("=" * 70)

    print(
        f"Saved metrics summary to:\n"
        f"{SUMMARY_FILE}"
    )


if __name__ == "__main__":
    main()