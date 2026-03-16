"""
Exercise 03: Chain-of-Thought A/B Test
========================================
Test chain-of-thought prompting on reasoning tasks and measure
the accuracy difference.

Setup:
    Use any LLM (free tier is fine).

Objectives:
    1. See when chain-of-thought actually helps (and when it doesn't)
    2. Practice adding CoT to prompts naturally
    3. Build intuition for when to use it in production

Why this matters:
    Chain-of-thought is free accuracy on reasoning tasks. It costs a few
    more output tokens but can turn a wrong answer into a right one.
    Knowing when to deploy it is a practical prompt engineering skill.
"""

# =============================================================================
# The Test Problems
# =============================================================================
#
# Each problem has a direct version and a CoT version.
# Run both through an LLM and record the answers.

PROBLEMS = [
    {
        "id": 1,
        "category": "math",
        "direct_prompt": (
            "A consultant bills $150/hour. They work 6 hours on Monday, "
            "4 hours on Tuesday, and 8 hours on Wednesday. On Thursday they "
            "have a half-day (4 hours) but 2 hours are non-billable internal "
            "meetings. What's the total billable amount for the week? "
            "Give just the dollar amount."
        ),
        "cot_prompt": (
            "A consultant bills $150/hour. They work 6 hours on Monday, "
            "4 hours on Tuesday, and 8 hours on Wednesday. On Thursday they "
            "have a half-day (4 hours) but 2 hours are non-billable internal "
            "meetings. What's the total billable amount for the week? "
            "Think through this step by step, then give the dollar amount."
        ),
        "correct_answer": "$3,000",
        "explanation": "6 + 4 + 8 + (4-2) = 20 billable hours × $150 = $3,000",
    },
    {
        "id": 2,
        "category": "logic",
        "direct_prompt": (
            "Three developers are assigned to a project. Alice can complete "
            "it alone in 10 days. Bob can complete it alone in 15 days. "
            "Carol can complete it alone in 20 days. If all three work "
            "together, approximately how many days will it take? "
            "Give just the number of days."
        ),
        "cot_prompt": (
            "Three developers are assigned to a project. Alice can complete "
            "it alone in 10 days. Bob can complete it alone in 15 days. "
            "Carol can complete it alone in 20 days. If all three work "
            "together, approximately how many days will it take? "
            "Work through the math step by step, then give the number of days."
        ),
        "correct_answer": "~4.6 days",
        "explanation": "Combined rate: 1/10 + 1/15 + 1/20 = 6/60 + 4/60 + 3/60 = 13/60 per day. Days = 60/13 ≈ 4.6",
    },
    {
        "id": 3,
        "category": "code_reasoning",
        "direct_prompt": (
            "What does this Python code print?\n\n"
            "x = [1, 2, 3, 4, 5]\n"
            "y = x[1:4]\n"
            "y[0] = 99\n"
            "print(x[1], y[0])\n\n"
            "Give just the output."
        ),
        "cot_prompt": (
            "What does this Python code print?\n\n"
            "x = [1, 2, 3, 4, 5]\n"
            "y = x[1:4]\n"
            "y[0] = 99\n"
            "print(x[1], y[0])\n\n"
            "Trace through the code line by line, then give the output."
        ),
        "correct_answer": "2 99",
        "explanation": "Slicing creates a new list, so modifying y doesn't affect x. x[1] is still 2, y[0] is 99.",
    },
    {
        "id": 4,
        "category": "analysis",
        "direct_prompt": (
            "A client's web app gets 10,000 requests/day. Each request calls "
            "an LLM API with ~500 input tokens and ~200 output tokens. "
            "Input costs $3/million tokens, output costs $15/million tokens. "
            "What's the monthly API cost (30 days)? Give just the dollar amount."
        ),
        "cot_prompt": (
            "A client's web app gets 10,000 requests/day. Each request calls "
            "an LLM API with ~500 input tokens and ~200 output tokens. "
            "Input costs $3/million tokens, output costs $15/million tokens. "
            "What's the monthly API cost (30 days)? "
            "Calculate this step by step, then give the dollar amount."
        ),
        "correct_answer": "$1,350/month",
        "explanation": (
            "Daily input: 10,000 × 500 = 5M tokens → $15/day. "
            "Daily output: 10,000 × 200 = 2M tokens → $30/day. "
            "Daily total: $45. Monthly: $45 × 30 = $1,350."
        ),
    },
    {
        "id": 5,
        "category": "simple_factual",
        "direct_prompt": "What programming language is pandas written in? Give just the language name.",
        "cot_prompt": "What programming language is pandas written in? Think step by step, then give the language name.",
        "correct_answer": "Python",
        "explanation": "This is a simple factual question — CoT shouldn't help (and might hurt by overcomplicating). Accept 'Python' with or without the 'with C extensions' qualifier.",
    },
]


# =============================================================================
# Part 1: Run the A/B Test
# =============================================================================

# TODO: For each problem, run both the direct and CoT versions.
# Record the model's answers below.

results = []
for problem in PROBLEMS:
    result = {
        "id": problem["id"],
        "category": problem["category"],
        "correct_answer": problem["correct_answer"],
        "direct_answer": "",  # TODO: Fill in after testing
        "cot_answer": "",     # TODO: Fill in after testing
        "direct_correct": None,  # TODO: True/False
        "cot_correct": None,     # TODO: True/False
    }
    results.append(result)


# =============================================================================
# Part 2: Analyze the Results
# =============================================================================

# TODO: Calculate and print:
# 1. Direct prompting accuracy (X/5)
# 2. CoT prompting accuracy (X/5)
# 3. Which problems did CoT help with?
# 4. Did CoT ever make things worse? (Problem 5 is the test case)


# =============================================================================
# Part 3: Write Your CoT Guidelines
# =============================================================================

# TODO: Based on your results, fill in practical guidelines.

COT_GUIDELINES = """
Chain-of-Thought Prompting Guidelines
=======================================

USE CoT when:
- TODO: List scenarios where CoT improved results
-
-

SKIP CoT when:
- TODO: List scenarios where CoT didn't help or hurt
-
-

How to add CoT to a prompt:
- Simple: Add "Think through this step by step" at the end
- Better: TODO — what phrasing worked best in your testing?
- For code: TODO
- For math: TODO

Cost consideration:
- CoT adds roughly _____ extra output tokens per response
- Worth it when: _____
- Not worth it when: _____
"""

# TODO: Print your completed guidelines
# print(COT_GUIDELINES)
