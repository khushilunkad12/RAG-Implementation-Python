print("EVALUATE.PY STARTED")
import os
import sys
import time
import pandas as pd

from datasets import Dataset
from ragas import evaluate

from ragas.metrics import (
    faithfulness,
    answer_relevancy
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
from sample_dataset import evaluation_dataset
from ragas_config import llm, embeddings

# ==========================================
# Generate Evaluation Dataset
# ==========================================

results = []

print("=" * 70)
print("Running Evaluation Dataset...")
print("=" * 70)

for sample in evaluation_dataset:

    question = sample["question"]
    ground_truth = sample["ground_truth"]

    print(f"\nQuestion: {question}")

    answer, metadata, documents, distances = generate_answer(question)

    results.append(
        {
            "question": question,
            "answer": answer,
            "contexts": documents,
            "ground_truth": ground_truth,
        }
    )

    print("✓ Completed")

    # Prevent Gemini rate limit
    time.sleep(5)

print("\nEvaluation Dataset Created!")

# ==========================================
# Convert to HuggingFace Dataset
# ==========================================

dataset = Dataset.from_pandas(
    pd.DataFrame(results)
)

# ==========================================
# Metrics
# ==========================================



# ==========================================
# Run Evaluation
# ==========================================

print("\n")
print("=" * 70)
print("Running RAGAS Evaluation...")
print("=" * 70)

scores = evaluate(
    dataset=dataset,
    metrics=[
        faithfulness,
        answer_relevancy
    ],
    llm=llm,
    embeddings=embeddings
)

print("\n")
print("=" * 70)
print("FINAL SCORES")
print("=" * 70)

print(scores)

# ==========================================
# Save Results
# ==========================================

scores_df = scores.to_pandas()

scores_df.to_csv(
    "evaluation_results.csv",
    index=False
)

print("\nResults saved as evaluation_results.csv")