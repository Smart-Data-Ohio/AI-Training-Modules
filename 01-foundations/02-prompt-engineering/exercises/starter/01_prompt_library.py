"""
Exercise 01: Prompt Library Builder
=====================================
Build structured prompts for 5 common consulting tasks.

Setup:
    Use any LLM (free tier is fine) to test your prompts.

Objectives:
    1. Practice structuring prompts with role, context, task, format, constraints
    2. Create reusable prompts that produce consistent outputs
    3. Build the start of a prompt library you can actually use at work

Why this matters:
    A tested prompt library is a consulting team's secret weapon. It turns
    AI from a toy into a tool — new developers get reliable results on day one.
"""


def build_prompt(role: str, context: str, task: str, output_format: str, constraints: list[str]) -> str:
    """Assemble a structured prompt from components.

    Args:
        role: Who the model should act as.
        context: Background information for the task.
        task: What specifically the model should do.
        output_format: How the output should be structured.
        constraints: List of things the model should NOT do or limits to follow.

    Returns:
        A complete, structured prompt string.
    """
    # TODO: Combine the components into a well-formatted prompt string.
    # Think about ordering — what should come first?
    # Consider using markdown headers or clear separators.
    pass


# =============================================================================
# Task 1: Code Review Prompt
# =============================================================================

# TODO: Build a prompt that reviews a code snippet for quality issues.
# The prompt should produce structured output (not just prose).
# Test it with a real code snippet.

code_review_prompt = build_prompt(
    role="",        # TODO
    context="",     # TODO
    task="",        # TODO
    output_format="",  # TODO: Specify a structured output format (JSON, markdown, etc.)
    constraints=[], # TODO
)


# =============================================================================
# Task 2: Meeting Summary Prompt
# =============================================================================

# TODO: Build a prompt that summarizes a meeting transcript.
# Focus on: decisions made, action items, and open questions.

meeting_summary_prompt = build_prompt(
    role="",
    context="",
    task="",
    output_format="",
    constraints=[],
)


# =============================================================================
# Task 3: Requirements Extraction Prompt
# =============================================================================

# TODO: Build a prompt that extracts technical requirements from a
# client email or conversation transcript.

requirements_prompt = build_prompt(
    role="",
    context="",
    task="",
    output_format="",
    constraints=[],
)


# =============================================================================
# Task 4: Bug Report Triage Prompt
# =============================================================================

# TODO: Build a prompt that triages a bug report — classifies severity,
# identifies likely component, and suggests investigation steps.

bug_triage_prompt = build_prompt(
    role="",
    context="",
    task="",
    output_format="",
    constraints=[],
)


# =============================================================================
# Task 5: Status Update Prompt
# =============================================================================

# TODO: Build a prompt that generates a client-ready status update
# from a developer's rough notes.

status_update_prompt = build_prompt(
    role="",
    context="",
    task="",
    output_format="",
    constraints=[],
)


# =============================================================================
# Testing Your Prompts
# =============================================================================

# TODO: Test at least 2 of your prompts with real or realistic input.
# For each test:
#   1. Print the full prompt
#   2. Run it through an LLM
#   3. Evaluate: Does the output match your format? Is it useful?
#   4. Iterate: What would you change?

# Example test input for the code review prompt:
sample_code = '''
def get_user(id):
    query = f"SELECT * FROM users WHERE id = {id}"
    result = db.execute(query)
    if result:
        return result[0]
    return None
'''

# TODO: Insert sample_code into your code review prompt and test it
