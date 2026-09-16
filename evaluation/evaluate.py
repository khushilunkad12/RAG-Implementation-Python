import os
import sys
import time
import json
import pandas as pd

from datasets import Dataset
from ragas import evaluate
from ragas.run_config import RunConfig
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall
)

# ==========================================
# Add Project Root
# ==========================================

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from rag_answer import generate_answer
from ragas_config import llm, embeddings


# ==========================================
# Load Fixed Evaluation Questions
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

EVAL_QUESTIONS_PATH = os.path.join(
    BASE_DIR,
    "eval_questions.json"
)

with open(EVAL_QUESTIONS_PATH, "r", encoding="utf-8") as f:
    evaluation_dataset = json.load(f)


print("=" * 70)
print("RAGAS Regression Evaluation")
print("=" * 70)

print(f"Evaluation questions loaded: {len(evaluation_dataset)}")
print(f"Dataset: {EVAL_QUESTIONS_PATH}")


# ==========================================
# Generate Evaluation Dataset
# ==========================================

results = []
chat_history = []

for index, sample in enumerate(evaluation_dataset, start=1):

    question = sample["question"]
    ground_truth = sample["ground_truth"]

    print("\n" + "-" * 70)
    print(f"Question {index}/{len(evaluation_dataset)}")
    print(f"Question: {question}")

    answer, metadata, documents, distances, rewritten_query = generate_answer(
        question,
        chat_history
    )

    results.append(
        {
            "question": question,
            "rewritten_query": rewritten_query,
            "retrieved_top_1": documents[0] if documents else "",
            "answer": answer,
            "contexts": documents,
            "ground_truth": ground_truth
        }
    )

    print("✓ Completed")

    # Prevent API rate limits
    time.sleep(10)


print("\nEvaluation dataset generated successfully.")


# ==========================================
# Convert to HuggingFace Dataset
# ==========================================

dataset = Dataset.from_pandas(
    pd.DataFrame(results)
)


# ==========================================
# Run RAGAS Evaluation
# ==========================================

print("\n")
print("=" * 70)
print("Running RAGAS Evaluation...")
print("=" * 70)

scores = evaluate(
    dataset=dataset,
    metrics=[
        answer_relevancy,
        faithfulness,
        context_precision,
        context_recall
    ],
    llm=llm,
    embeddings=embeddings,
    run_config=RunConfig(
        max_workers=1,
        timeout=600,
        max_retries=5
    ),
    raise_exceptions=False
)


# ==========================================
# Print Final Scores
# ==========================================

print("\n")
print("=" * 70)
print("FINAL RAGAS BASELINE SCORES")
print("=" * 70)

print(scores)


# ==========================================
# Save Results
# ==========================================

scores_df = scores.to_pandas()

OUTPUT_PATH = os.path.join(
    BASE_DIR,
    "evaluation_results.csv"
)

scores_df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("\nResults saved to:")
print(OUTPUT_PATH)

print("\n" + "=" * 70)
print("RAGAS BASELINE EVALUATION COMPLETED")
print("=" * 70)