"""
Exercise 03: Chain-of-Thought A/B Test — Solution
===================================================
Example results and completed guidelines.
"""

# =============================================================================
# Example Results
# =============================================================================

# Representative results from testing with Claude 3.5 Sonnet:

results = [
    {
        "id": 1,
        "category": "math",
        "correct_answer": "$3,000",
        "direct_answer": "$3,000",
        "cot_answer": "$3,000",
        "direct_correct": True,
        "cot_correct": True,
        "notes": "Both got it right. The math is straightforward enough.",
    },
    {
        "id": 2,
        "category": "logic",
        "correct_answer": "~4.6 days",
        "direct_answer": "5 days",
        "cot_answer": "4.6 days",
        "direct_correct": False,
        "cot_correct": True,
        "notes": "Direct answer rounded incorrectly. CoT showed the work rates calculation and got the precise answer.",
    },
    {
        "id": 3,
        "category": "code_reasoning",
        "correct_answer": "2 99",
        "direct_answer": "99 99",
        "cot_answer": "2 99",
        "direct_correct": False,
        "cot_correct": True,
        "notes": "Direct answer assumed slicing creates a reference (like in some languages). CoT correctly traced through Python's slice-copy behavior.",
    },
    {
        "id": 4,
        "category": "analysis",
        "correct_answer": "$1,350/month",
        "direct_answer": "$1,350",
        "cot_answer": "$1,350",
        "direct_correct": True,
        "cot_correct": True,
        "notes": "Both correct. The CoT version showed clearer intermediate steps, which is useful for verifying the answer.",
    },
    {
        "id": 5,
        "category": "simple_factual",
        "correct_answer": "Python",
        "direct_answer": "Python",
        "cot_answer": "Python",
        "direct_correct": True,
        "cot_correct": True,
        "notes": "Both correct. CoT added unnecessary explanation about C extensions and Cython — more tokens for no benefit.",
    },
]

# =============================================================================
# Analysis
# =============================================================================

direct_correct = sum(1 for r in results if r["direct_correct"])
cot_correct = sum(1 for r in results if r["cot_correct"])

print("=" * 60)
print("Chain-of-Thought A/B Test Results")
print("=" * 60)
print(f"\n  Direct prompting: {direct_correct}/5 correct ({direct_correct/5:.0%})")
print(f"  CoT prompting:    {cot_correct}/5 correct ({cot_correct/5:.0%})")
print(f"\n  CoT improved: {cot_correct - direct_correct} answers")

print("\n  Breakdown by problem:")
for r in results:
    direct_mark = "✓" if r["direct_correct"] else "✗"
    cot_mark = "✓" if r["cot_correct"] else "✗"
    print(f"    {r['id']}. [{r['category']:20s}] Direct: {direct_mark}  CoT: {cot_mark}")
    if r["direct_correct"] != r["cot_correct"]:
        print(f"       ^ CoT made the difference: {r['notes']}")

# =============================================================================
# Guidelines
# =============================================================================

COT_GUIDELINES = """
Chain-of-Thought Prompting Guidelines
=======================================

USE CoT when:
- Multi-step math or calculations (rates, costs, compound operations)
- Code tracing/debugging (follow execution path step by step)
- Logic problems with multiple interacting constraints
- Any task where intermediate steps affect the final answer

SKIP CoT when:
- Simple factual recall ("What language is pandas written in?")
- Classification tasks (few-shot examples are more effective)
- Creative writing (CoT makes it outline instead of write)
- When you don't need to verify the reasoning (and token cost matters)

How to add CoT to a prompt:
- Simple: "Think through this step by step."
- For math: "Show your calculations step by step, then give the final answer."
- For code: "Trace through this code line by line, tracking variable values."
- For analysis: "Consider each factor separately, then synthesize."

Cost consideration:
- CoT adds roughly 100-300 extra output tokens per response
- Worth it when: accuracy matters more than speed/cost (client deliverables,
  financial calculations, code analysis)
- Not worth it when: high-volume, simple tasks where the overhead adds up
  (e.g., classifying 10,000 support tickets — use few-shot instead)

Production tip:
- You can use CoT for reasoning but strip the reasoning from the user-facing
  output. Ask the model to put its reasoning in <thinking> tags and the
  final answer outside them, then parse accordingly.
"""

print(COT_GUIDELINES)
