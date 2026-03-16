"""
Exercise 02: Few-Shot vs Zero-Shot Comparison
===============================================
Compare the output quality of zero-shot and few-shot prompting
on a classification task.

Setup:
    Use any LLM (free tier is fine).

Objectives:
    1. See the measurable difference between zero-shot and few-shot
    2. Learn how to pick good few-shot examples
    3. Understand when few-shot is worth the extra tokens

Why this matters:
    A 25% accuracy improvement from adding 3 examples to a prompt
    can be the difference between a feature that works and one that
    doesn't. This is low-hanging fruit in every AI integration.
"""

# =============================================================================
# The Task: Support Ticket Classification
# =============================================================================
#
# Classify customer support messages into these categories:
#   - billing     (payment issues, charges, refunds, invoices)
#   - technical   (bugs, errors, outages, integration problems)
#   - feature     (requests for new features or improvements)
#   - account     (login issues, permissions, profile changes)
#   - general     (everything else)

CATEGORIES = ["billing", "technical", "feature", "account", "general"]

# These are the test messages. You'll classify them with both approaches.
TEST_MESSAGES = [
    "I was charged twice for my subscription this month.",
    "The export button gives a 500 error when I try to download CSV files.",
    "It would be great if the dashboard could show weekly trends.",
    "I can't log in even after resetting my password three times.",
    "Do you have any documentation on your API rate limits?",
    "Our team needs to add 5 more seats but the upgrade page is broken.",
    "When will you support dark mode? It's 2026, come on.",
    "My invoice from February still shows the old company name.",
    "The mobile app crashes every time I try to upload a photo.",
    "Can my manager get read-only access to my reports?",
]

# The correct answers (for scoring):
CORRECT_LABELS = [
    "billing",      # charged twice
    "technical",    # 500 error
    "feature",      # weekly trends request
    "account",      # login issues
    "general",      # documentation question
    "technical",    # upgrade page broken (billing context but technical issue)
    "feature",      # dark mode request
    "billing",      # invoice issue
    "technical",    # app crash
    "account",      # access permissions
]


# =============================================================================
# Part 1: Zero-Shot Classification
# =============================================================================

# TODO: Write a zero-shot prompt that classifies a support message into
# one of the CATEGORIES. No examples — just the task description.

ZERO_SHOT_PROMPT_TEMPLATE = """
TODO: Write your zero-shot prompt here. Your prompt should:
  1. List the categories with brief descriptions so the model knows what each means
  2. Include the message to classify (use {message} as a placeholder)
  3. Tell the model to respond with ONLY the category label, nothing else

Skeleton to get you started:
  Classify the following customer support message into exactly one category.

  Categories:
  - billing: ...
  - technical: ...
  (fill in the rest)

  Message: {message}
  Category:
"""


def classify_zero_shot(message: str) -> str:
    """Classify a message using the zero-shot prompt.

    TODO: Either call an LLM API programmatically, or run each
    message manually and record the results below.
    """
    # TODO: Implement or use manual testing
    pass


# TODO: Record zero-shot results here (if testing manually)
zero_shot_results = [
    "",  # Message 1 result
    "",  # Message 2 result
    "",  # ...
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]


# =============================================================================
# Part 2: Few-Shot Classification
# =============================================================================

# TODO: Write a few-shot prompt with 2-3 examples per category.
# Choose examples that are DIFFERENT from the test messages.
# Pick examples that cover edge cases and tricky boundaries.

FEW_SHOT_PROMPT_TEMPLATE = """
TODO: Write your few-shot prompt here.
Include examples for each category.
Use {message} as a placeholder for the test message.

Examples:

Message: "..."
Category: billing

Message: "..."
Category: technical

(add more examples)

Now classify:
Message: {message}
Category:
"""


def classify_few_shot(message: str) -> str:
    """Classify a message using the few-shot prompt."""
    # TODO: Implement or use manual testing
    pass


# TODO: Record few-shot results here (if testing manually)
few_shot_results = [
    "",  # Message 1 result
    "",  # Message 2 result
    "",  # ...
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]


# =============================================================================
# Part 3: Score and Compare
# =============================================================================

def score_results(predictions: list[str], actuals: list[str]) -> dict:
    """Calculate accuracy and identify misclassifications.

    Args:
        predictions: List of predicted categories.
        actuals: List of correct categories.

    Returns:
        Dict with accuracy score and list of misclassified items.
    """
    # TODO: Calculate the accuracy (correct / total)
    # TODO: Build a list of misclassified items with index, predicted, actual
    # TODO: Return results as a dict
    pass


# TODO: Score both approaches and print a comparison
# zero_shot_score = score_results(zero_shot_results, CORRECT_LABELS)
# few_shot_score = score_results(few_shot_results, CORRECT_LABELS)

# TODO: Print a summary answering these questions:
# 1. What was the accuracy for each approach?
# 2. Which messages were misclassified by zero-shot but correct with few-shot?
# 3. Were there any messages that few-shot got WRONG that zero-shot got right?
# 4. Was the improvement worth the extra tokens? (estimate the token cost difference)
