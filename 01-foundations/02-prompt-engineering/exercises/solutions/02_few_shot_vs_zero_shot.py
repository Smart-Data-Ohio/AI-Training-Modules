"""
Exercise 02: Few-Shot vs Zero-Shot — Solution
===============================================
Demonstrates well-structured zero-shot and few-shot prompts
with example results and analysis.
"""

CATEGORIES = ["billing", "technical", "feature", "account", "general"]

CORRECT_LABELS = [
    "billing", "technical", "feature", "account", "general",
    "technical", "feature", "billing", "technical", "account",
]

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

# =============================================================================
# Zero-Shot Prompt
# =============================================================================

ZERO_SHOT_PROMPT_TEMPLATE = """Classify the following customer support message into exactly one category.

Categories:
- billing: payment issues, charges, refunds, invoices
- technical: bugs, errors, outages, integration problems
- feature: requests for new features or improvements
- account: login issues, permissions, profile changes
- general: everything else

Respond with ONLY the category label, nothing else.

Message: {message}
Category:"""

# =============================================================================
# Few-Shot Prompt
# =============================================================================

FEW_SHOT_PROMPT_TEMPLATE = """Classify customer support messages into one of these categories:
billing, technical, feature, account, general.

Examples:

Message: "I see a charge of $49.99 on my credit card but I cancelled last month."
Category: billing

Message: "The page won't load — I keep getting a spinning wheel that never stops."
Category: technical

Message: "Any plans to add Slack integration? Would save our team a lot of time."
Category: feature

Message: "I need to change the email address associated with my account."
Category: account

Message: "What are your office hours for phone support?"
Category: general

Message: "The billing page shows an error when I try to update my card."
Category: technical

Message: "Can I get a copy of last quarter's invoices for our accountant?"
Category: billing

Now classify:
Message: {message}
Category:"""

# Note: The few-shot prompt includes a tricky example — "billing page shows
# an error" is categorized as "technical" because the issue is a broken page,
# not a billing dispute. This teaches the model to look at the actual problem,
# not just keywords.


# =============================================================================
# Example Results
# =============================================================================

# These are representative results from Claude 3.5 Sonnet:

zero_shot_results = [
    "billing",      # ✓ charged twice
    "technical",    # ✓ 500 error
    "feature",      # ✓ weekly trends
    "account",      # ✓ login issues
    "general",      # ✓ documentation
    "billing",      # ✗ upgrade page broken → should be technical
    "feature",      # ✓ dark mode
    "billing",      # ✓ invoice issue
    "technical",    # ✓ app crash
    "account",      # ✓ access permissions
]

few_shot_results = [
    "billing",      # ✓ charged twice
    "technical",    # ✓ 500 error
    "feature",      # ✓ weekly trends
    "account",      # ✓ login issues
    "general",      # ✓ documentation
    "technical",    # ✓ upgrade page broken (tricky — few-shot example helped!)
    "feature",      # ✓ dark mode
    "billing",      # ✓ invoice issue
    "technical",    # ✓ app crash
    "account",      # ✓ access permissions
]


# =============================================================================
# Scoring
# =============================================================================

def score_results(predictions: list[str], actuals: list[str]) -> dict:
    """Calculate accuracy and identify misclassifications."""
    correct = sum(1 for p, a in zip(predictions, actuals) if p == a)
    total = len(actuals)

    misclassified = []
    for i, (pred, actual) in enumerate(zip(predictions, actuals)):
        if pred != actual:
            misclassified.append({
                "index": i,
                "message_preview": TEST_MESSAGES[i][:60] + "...",
                "predicted": pred,
                "actual": actual,
            })

    return {
        "accuracy": correct / total,
        "correct": correct,
        "total": total,
        "misclassified": misclassified,
    }


zero_score = score_results(zero_shot_results, CORRECT_LABELS)
few_score = score_results(few_shot_results, CORRECT_LABELS)

print("=" * 60)
print("Few-Shot vs Zero-Shot: Results")
print("=" * 60)
print(f"\n  Zero-shot accuracy: {zero_score['accuracy']:.0%} ({zero_score['correct']}/{zero_score['total']})")
print(f"  Few-shot accuracy:  {few_score['accuracy']:.0%} ({few_score['correct']}/{few_score['total']})")
print(f"\n  Improvement: +{(few_score['accuracy'] - zero_score['accuracy']):.0%}")

if zero_score["misclassified"]:
    print("\n  Zero-shot misclassifications:")
    for m in zero_score["misclassified"]:
        print(f"    [{m['index']}] \"{m['message_preview']}\"")
        print(f"         Predicted: {m['predicted']}, Actual: {m['actual']}")

print("\n" + "=" * 60)
print("Key Insight")
print("=" * 60)
print("""
  The tricky message was #6: "upgrade page is broken"
  It mentions billing context (adding seats) but the actual
  problem is technical (broken page). The few-shot prompt
  included a similar edge case example, which taught the model
  to classify by the problem type, not by keywords.

  This is why few-shot examples should cover edge cases,
  not just obvious examples.
""")
