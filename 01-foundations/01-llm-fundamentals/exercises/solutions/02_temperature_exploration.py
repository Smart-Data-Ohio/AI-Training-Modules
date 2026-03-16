"""
Exercise 02: Temperature Exploration — Solution
=================================================
This solution shows the structure with example observations.
Your actual results will vary — that's the point of the exercise.
"""

# NOTE: This solution file demonstrates what completed observations
# and a cheat sheet look like. Your specific results will differ
# depending on which model you used and when you ran the experiment.

OBSERVATIONS = {
    "factual": {
        "temp_0": "Identical answers every time. 'The capital of France is Paris.'",
        "temp_05": "Same core answer, minor wording variation. Still correct.",
        "temp_1": "Answer still correct but phrasing varies more. Occasionally adds unsolicited context.",
        "best_temp": 0,
        "why": "Factual questions have one right answer. No reason to introduce randomness.",
    },
    "creative": {
        "temp_0": "Decent but generic. Same description every time — feels like a template.",
        "temp_05": "More variety between runs. Better word choices. Feels more human.",
        "temp_1": "Most creative phrasing but occasionally goes off-track or gets flowery.",
        "best_temp": 0.7,
        "why": "Creative tasks benefit from variety, but 1.0 can produce unfocused results. 0.7 is the sweet spot.",
    },
    "code": {
        "temp_0": "Clean, consistent implementation. Same approach every time.",
        "temp_05": "Minor variations (variable names, slightly different logic) but all functional.",
        "temp_1": "Sometimes picks unusual approaches. Occasionally introduces subtle bugs.",
        "best_temp": 0,
        "why": "Code needs to work. Creativity in code generation usually means unpredictability.",
    },
    "classification": {
        "temp_0": "Always returns 'complaint'. Consistent and correct.",
        "temp_05": "Usually 'complaint', occasionally adds explanation or hedging.",
        "temp_1": "Sometimes waffles between categories or adds unnecessary caveats.",
        "best_temp": 0,
        "why": "Classification is deterministic. You want the same input to always produce the same label.",
    },
    "analysis": {
        "temp_0": "Same three risks every time. Reasonable but not comprehensive.",
        "temp_05": "Different risks surface across runs. Broader coverage overall.",
        "temp_1": "Some novel insights but occasionally includes implausible risks.",
        "best_temp": 0.3,
        "why": "Analysis benefits from some variety to surface different perspectives, but needs to stay grounded.",
    },
}

CHEAT_SHEET = """
Temperature Cheat Sheet
========================

Task Type           | Recommended Temp | Why
--------------------|-----------------|----
Data extraction     | 0               | One right answer, need consistency
Code generation     | 0               | Code must be correct and predictable
Classification      | 0               | Same input should always get same label
Summarization       | 0 - 0.2         | Stick to the source material
Translation         | 0 - 0.2         | Accuracy over creativity
Analysis            | 0.3 - 0.5       | Some variety helps surface insights
Creative writing    | 0.7 - 0.9       | Want genuine variation and personality
Brainstorming       | 0.8 - 1.0       | More randomness = more diverse ideas

General rules:
  - Start at 0, only increase when you have a reason
  - If you need the same answer every time: temp 0
  - If you want variety but not chaos: temp 0.3-0.7
  - If you want maximum creativity: temp 0.8-1.0
  - Above 1.0 is almost never useful in production
"""

print(CHEAT_SHEET)
