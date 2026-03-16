"""
Exercise 02: Temperature Exploration
======================================
Explore how temperature affects LLM output by running the same prompts
at different temperature settings.

Setup:
    Option A (recommended): Use a free LLM playground
        - https://chat.openai.com (free tier)
        - https://claude.ai (free tier)
        - https://console.anthropic.com/workbench (API playground, free credits)

    Option B: Use the OpenAI or Anthropic Python SDK
        pip install openai
        # or
        pip install anthropic

    If using the SDK, you'll need an API key set as an environment variable:
        export OPENAI_API_KEY="your-key-here"
        # or
        export ANTHROPIC_API_KEY="your-key-here"

Objectives:
    1. Observe how temperature changes output for the SAME prompt
    2. Identify which tasks benefit from low vs high temperature
    3. Develop intuition for choosing the right temperature in production

Why this matters:
    Temperature is one of the most impactful parameters you can tune, and
    most developers never touch it. Knowing when to use 0 vs 0.7 is the
    difference between a reliable tool and a frustrating one.
"""

# =============================================================================
# Part 1: Temperature Comparison (Manual or API)
# =============================================================================
#
# For each prompt below, run it at temperature 0, 0.5, and 1.0.
# At each temperature, run it at least twice to see whether the output
# varies between runs. Record your observations in the OBSERVATIONS dict below.
#
# If using a playground: adjust the temperature slider and regenerate.
# If using the API: use the function template below.

PROMPTS = {
    "factual": "What is the capital of France? Answer in one sentence.",

    "creative": "Write a one-paragraph product description for a smart water bottle that tracks hydration.",

    "code": "Write a Python function that checks if a string is a palindrome.",

    "classification": "Classify the following customer message as 'complaint', 'question', or 'praise': "
                      "'I've been waiting 3 weeks for my order and nobody has responded to my emails.'",

    "analysis": "What are three potential risks of using AI in healthcare? List them briefly.",
}

TEMPERATURES = [0, 0.5, 1.0]


def call_llm(prompt: str, temperature: float) -> str:
    """Call an LLM API with a specific temperature setting.

    TODO: Implement this using your preferred API, OR do this exercise
    manually using a playground UI.

    Example using Anthropic:
        import anthropic
        client = anthropic.Anthropic()
        message = client.messages.create(
            model="claude-sonnet-4-5-20250514",
            max_tokens=256,
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text

    Example using OpenAI:
        from openai import OpenAI
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=256,
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    """
    # TODO: Implement API call or return placeholder for manual testing
    pass


# TODO: For each prompt, call the LLM at each temperature 3 times.
# Print the results in a readable format so you can compare.
#
# for prompt_name, prompt_text in PROMPTS.items():
#     print(f"\n{'='*60}")
#     print(f"Prompt: {prompt_name}")
#     print(f"{'='*60}")
#     for temp in TEMPERATURES:
#         print(f"\n  Temperature: {temp}")
#         for run in range(3):
#             result = call_llm(prompt_text, temp)
#             print(f"    Run {run+1}: {result[:100]}...")


# =============================================================================
# Part 2: Record Your Observations
# =============================================================================

# TODO: Fill in your observations after running the experiments above.

OBSERVATIONS = {
    "factual": {
        "temp_0": "",   # What did you notice at temperature 0?
        "temp_05": "",  # What changed at 0.5?
        "temp_1": "",   # What about 1.0?
        "best_temp": 0, # Which temperature would you use in production?
        "why": "",      # Why?
    },
    "creative": {
        "temp_0": "",
        "temp_05": "",
        "temp_1": "",
        "best_temp": 0,
        "why": "",
    },
    "code": {
        "temp_0": "",
        "temp_05": "",
        "temp_1": "",
        "best_temp": 0,
        "why": "",
    },
    "classification": {
        "temp_0": "",
        "temp_05": "",
        "temp_1": "",
        "best_temp": 0,
        "why": "",
    },
    "analysis": {
        "temp_0": "",
        "temp_05": "",
        "temp_1": "",
        "best_temp": 0,
        "why": "",
    },
}


# =============================================================================
# Part 3: Temperature Cheat Sheet
# =============================================================================

# TODO: Based on your experiments, fill in this cheat sheet.
# This is something you'd actually reference on real projects.

CHEAT_SHEET = """
Temperature Cheat Sheet
========================

Task Type           | Recommended Temp | Why
--------------------|-----------------|----
Data extraction     |                 |
Code generation     |                 |
Classification      |                 |
Creative writing    |                 |
Brainstorming       |                 |
Summarization       |                 |
Translation         |                 |
"""

# TODO: Print your completed cheat sheet
# print(CHEAT_SHEET)
