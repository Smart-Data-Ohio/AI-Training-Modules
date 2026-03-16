"""
Exercise 01: Token Counting
============================
Use the `tiktoken` library to explore how different types of text tokenize.

Setup:
    pip install tiktoken

Objectives:
    1. Count tokens for different types of input text
    2. Compare tokenization across different encodings
    3. Understand why token count matters for cost estimation

Why this matters:
    Every API call is billed per token. If you can't estimate token counts,
    you can't estimate costs — and that's a bad place to be in a client proposal.
"""

import tiktoken


def count_tokens(text: str, model: str = "gpt-4") -> int:
    """Count the number of tokens in a text string for a given model.

    Args:
        text: The input text to tokenize.
        model: The model whose tokenizer to use (e.g., "gpt-4", "gpt-3.5-turbo").

    Returns:
        The number of tokens.
    """
    # TODO: Get the encoding for the specified model using tiktoken.encoding_for_model()
    # TODO: Encode the text and return the number of tokens
    pass


def show_tokens(text: str, model: str = "gpt-4") -> list[str]:
    """Show the individual tokens that a text string is broken into.

    Args:
        text: The input text to tokenize.
        model: The model whose tokenizer to use.

    Returns:
        A list of token strings.
    """
    # TODO: Get the encoding for the specified model
    # TODO: Encode the text to get token IDs
    # TODO: Decode each token ID individually to see the actual token strings
    # HINT: Use encoding.decode([token_id]) for each token
    pass


def estimate_cost(text: str, cost_per_million_tokens: float = 3.00) -> float:
    """Estimate the API cost for processing a text input.

    Args:
        text: The input text.
        cost_per_million_tokens: The price per 1M input tokens (varies by model).

    Returns:
        Estimated cost in dollars.
    """
    # TODO: Count the tokens
    # TODO: Calculate cost based on tokens / 1_000_000 * cost_per_million_tokens
    pass


# =============================================================================
# Part 1: Basic Token Counting
# =============================================================================

# TODO: Count tokens for each of these strings and print the results.
# Pay attention to which ones surprise you.

test_strings = [
    "Hello, world!",
    "Supercalifragilisticexpialidocious",
    "こんにちは世界",  # "Hello, world" in Japanese
    "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)",
    "The quick brown fox jumps over the lazy dog.",
    "   ",  # Just spaces
    "🎉🎊🎈",  # Emojis
    "123456789",
    "1,234,567.89",
]

# TODO: Loop through test_strings, count tokens for each, and print results
# Example output: "'Hello, world!' -> 4 tokens"


# =============================================================================
# Part 2: See the Actual Tokens
# =============================================================================

# TODO: Pick 3 strings from above that had surprising token counts.
# Use show_tokens() to see how they were actually split.
# Print each token on its own line so you can see the boundaries.


# =============================================================================
# Part 3: Cost Estimation
# =============================================================================

# Here's a realistic scenario: a client wants to process customer support emails.
# They get about 500 emails per day, averaging 200 words each.

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

# TODO: Count tokens in the sample email
# TODO: Estimate the daily cost if processing 500 similar emails
#        Use $3.00 per million tokens (input) as the rate
# TODO: Estimate the monthly cost (assume 22 business days)
# TODO: Print a summary that would be useful in a client proposal
