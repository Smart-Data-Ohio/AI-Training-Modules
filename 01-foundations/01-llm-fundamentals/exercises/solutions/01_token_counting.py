"""
Exercise 01: Token Counting — Solution
========================================
"""

import tiktoken


def count_tokens(text: str, model: str = "gpt-4") -> int:
    """Count the number of tokens in a text string for a given model."""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))


def show_tokens(text: str, model: str = "gpt-4") -> list[str]:
    """Show the individual tokens that a text string is broken into."""
    encoding = tiktoken.encoding_for_model(model)
    token_ids = encoding.encode(text)
    return [encoding.decode([tid]) for tid in token_ids]


def estimate_cost(text: str, cost_per_million_tokens: float = 3.00) -> float:
    """Estimate the API cost for processing a text input."""
    tokens = count_tokens(text, "gpt-4")
    return tokens / 1_000_000 * cost_per_million_tokens


# =============================================================================
# Part 1: Basic Token Counting
# =============================================================================

test_strings = [
    "Hello, world!",
    "Supercalifragilisticexpialidocious",
    "こんにちは世界",
    "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)",
    "The quick brown fox jumps over the lazy dog.",
    "   ",
    "🎉🎊🎈",
    "123456789",
    "1,234,567.89",
]

print("Part 1: Token Counts")
print("=" * 60)
for s in test_strings:
    display = s.replace("\n", "\\n")
    if len(display) > 50:
        display = display[:50] + "..."
    count = count_tokens(s)
    print(f"  {display!r:55s} -> {count} tokens")

# =============================================================================
# Part 2: See the Actual Tokens
# =============================================================================

print("\n\nPart 2: Token Breakdown")
print("=" * 60)

interesting = [
    "Supercalifragilisticexpialidocious",
    "こんにちは世界",
    "🎉🎊🎈",
]

for s in interesting:
    tokens = show_tokens(s)
    print(f"\n  {s!r}")
    print(f"  Tokens ({len(tokens)}): {tokens}")

# =============================================================================
# Part 3: Cost Estimation
# =============================================================================

sample_email = """
Dear Support Team,

I'm writing to report an issue with my recent order #12345. The package arrived
yesterday but was missing two items from my original order: the wireless mouse
and the USB-C hub. The keyboard and monitor stand were included and in good
condition.

I've attached photos of the package contents and the original order confirmation.
Could you please arrange for the missing items to be shipped? I need them for my
home office setup by next Friday if possible.

Thank you for your help,
Jane Smith
Account #JS-98765
"""

email_tokens = count_tokens(sample_email)
daily_tokens = email_tokens * 500
daily_cost = estimate_cost(sample_email) * 500
monthly_cost = daily_cost * 22

print("\n\nPart 3: Cost Estimation")
print("=" * 60)
print(f"  Tokens per email:     {email_tokens:,}")
print(f"  Daily tokens (500x):  {daily_tokens:,}")
print(f"  Daily cost:           ${daily_cost:.4f}")
print(f"  Monthly cost (22d):   ${monthly_cost:.2f}")
print()
print("  Client Proposal Summary:")
print("  ─────────────────────────")
print(f"  Processing 500 customer emails/day with GPT-4 input pricing")
print(f"  at $3.00/million tokens would cost approximately ${monthly_cost:.2f}/month")
print(f"  in input tokens alone. Output tokens and any additional API")
print(f"  calls (e.g., classification, response generation) would add")
print(f"  to this baseline cost.")
