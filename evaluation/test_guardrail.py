import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from rag_answer import generate_answer


GUARDRAIL_MESSAGE = "Not enough information in the uploaded documents."


def test_supported_question():
    question = "What is Python?"

    answer, metadata, documents, distances, rewritten_query = generate_answer(
        question
    )

    print("\nSupported Question:", question)
    print("Rewritten Query:", rewritten_query)
    print("Answer:", answer)

    assert answer.strip() != GUARDRAIL_MESSAGE, (
        "Supported question incorrectly triggered the guardrail."
    )

    print("✓ Supported question test passed")


def test_unsupported_question():
    question = "What is the capital of France?"

    answer, metadata, documents, distances, rewritten_query = generate_answer(
        question
    )

    print("\nUnsupported Question:", question)
    print("Rewritten Query:", rewritten_query)
    print("Answer:", answer)

    assert answer.strip() == GUARDRAIL_MESSAGE, (
        "Unsupported question did not trigger the guardrail."
    )

    print("✓ Unsupported question test passed")


if __name__ == "__main__":
    test_supported_question()
    test_unsupported_question()

    print("\n" + "=" * 60)
    print("ALL GUARDRAIL TESTS PASSED")
    print("=" * 60)