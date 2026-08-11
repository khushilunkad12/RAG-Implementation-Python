import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from rag_answer import generate_answer

questions = [
    "What is the time complexity of Python's dictionary lookup?",
    "What is the capital of France?",
    "How does Python handle quantum computing?"
]

for question in questions:
    print("\nQuestion:", question)

    answer, metadata, documents, distances = generate_answer(question)

    print("Answer:", answer)

    if answer.strip() == "Not enough information in the uploaded documents.":
        print("✓ Guardrail triggered")
    else:
        print("⚠ Answer generated")