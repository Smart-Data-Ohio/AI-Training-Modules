"""
Exercise 01: Prompt Library Builder — Solution
================================================
"""


def build_prompt(role: str, context: str, task: str, output_format: str, constraints: list[str]) -> str:
    """Assemble a structured prompt from components."""
    parts = []

    if role:
        parts.append(f"## Role\n{role}")
    if context:
        parts.append(f"## Context\n{context}")
    if task:
        parts.append(f"## Task\n{task}")
    if output_format:
        parts.append(f"## Output Format\n{output_format}")
    if constraints:
        constraint_text = "\n".join(f"- {c}" for c in constraints)
        parts.append(f"## Constraints\n{constraint_text}")

    return "\n\n".join(parts)


# =============================================================================
# Task 1: Code Review Prompt
# =============================================================================

code_review_prompt = build_prompt(
    role="You are a senior software engineer performing a code review. You focus on correctness, security, readability, and performance — in that order.",
    context="The code is part of a production web application used by a consulting client. It handles user-facing data.",
    task="Review the following code snippet. Identify issues and suggest improvements.",
    output_format="""Respond in this exact format:

## Issues Found

| # | Severity | Type | Description | Suggestion |
|---|----------|------|-------------|------------|
| 1 | critical/high/medium/low | bug/security/performance/style | What's wrong | How to fix it |

## Summary
One sentence: is this code safe to ship? What's the most important fix?""",
    constraints=[
        "Only flag real issues — don't nitpick style preferences",
        "If there are security issues, always list them first",
        "Be specific about fix suggestions — include code when possible",
        "If the code is fine, say so. Don't invent problems.",
    ],
)

# Test with the sample code
sample_code = '''
def get_user(id):
    query = f"SELECT * FROM users WHERE id = {id}"
    result = db.execute(query)
    if result:
        return result[0]
    return None
'''

print("=" * 60)
print("CODE REVIEW PROMPT")
print("=" * 60)
print(code_review_prompt)
print(f"\nCode to review:\n```python{sample_code}```")


# =============================================================================
# Task 2: Meeting Summary Prompt
# =============================================================================

meeting_summary_prompt = build_prompt(
    role="You are a project manager summarizing a meeting for stakeholders who weren't present.",
    context="This is an internal meeting at a software consulting company. The summary will be shared with the project team and potentially the client.",
    task="Summarize the following meeting transcript. Focus on what was decided, what needs to happen next, and what's still unresolved.",
    output_format="""## Meeting Summary — [Date/Topic]

**Attendees:** [list from transcript]

### Decisions Made
- Bulleted list of decisions with brief context

### Action Items
| Owner | Action | Deadline |
|-------|--------|----------|
| Name  | What   | When     |

### Open Questions
- Questions that weren't resolved, with who needs to answer them

### Key Quotes
- Any particularly important statements (with attribution)""",
    constraints=[
        "Keep the summary under 300 words (excluding the table)",
        "Don't editorialize — report what was said, not what you think about it",
        "If deadlines weren't mentioned, mark them as 'TBD'",
        "Flag any potential risks or concerns that were raised",
    ],
)


# =============================================================================
# Task 3: Requirements Extraction Prompt
# =============================================================================

requirements_prompt = build_prompt(
    role="You are a business analyst extracting technical requirements from a client conversation.",
    context="The client is a non-technical stakeholder describing what they want built. Requirements need to be clear enough for a developer to estimate and implement.",
    task="Extract technical requirements from the following client communication. Distinguish between explicit asks and implied needs.",
    output_format="""## Extracted Requirements

### Explicit Requirements (client directly asked for these)
| # | Requirement | Priority (inferred) | Notes |
|---|-------------|---------------------|-------|
| 1 | ...         | must-have/nice-to-have/unclear | ... |

### Implied Requirements (necessary but not explicitly stated)
| # | Requirement | Why it's needed |
|---|-------------|-----------------|
| 1 | ...         | ...             |

### Clarification Needed
- Questions to ask the client before proceeding

### Out of Scope (mentioned but likely separate work)
- Items that came up but should be separate projects/tickets""",
    constraints=[
        "Use the client's own language where possible",
        "Don't add technical implementation details — just the 'what', not the 'how'",
        "If something is ambiguous, list it under 'Clarification Needed' rather than guessing",
        "Be conservative with priority inference — when in doubt, mark as 'unclear'",
    ],
)


# =============================================================================
# Task 4: Bug Report Triage Prompt
# =============================================================================

bug_triage_prompt = build_prompt(
    role="You are a senior developer triaging incoming bug reports for a web application.",
    context="The application is a SaaS product with a React frontend, Python/FastAPI backend, and PostgreSQL database. The team uses severity levels: critical (production down), high (major feature broken), medium (feature degraded), low (cosmetic/minor).",
    task="Triage the following bug report. Classify its severity, identify the likely component, and suggest initial investigation steps.",
    output_format="""## Bug Triage

**Severity:** critical / high / medium / low
**Likely Component:** frontend / backend / database / infrastructure / unknown
**Reproducible:** yes / no / unclear from report

### Analysis
2-3 sentences on what's likely happening.

### Investigation Steps
1. First thing to check
2. Second thing to check
3. Third thing to check

### Questions for Reporter
- Anything needed to reproduce or understand the bug""",
    constraints=[
        "Err on the side of higher severity when uncertain",
        "Don't assume the reporter's diagnosis is correct — focus on symptoms",
        "Keep investigation steps actionable and specific (not 'check the logs')",
    ],
)


# =============================================================================
# Task 5: Status Update Prompt
# =============================================================================

status_update_prompt = build_prompt(
    role="You are a project lead writing a weekly status update for a client stakeholder.",
    context="The client is a non-technical executive. They care about progress, timelines, and risks — not technical details. The tone should be professional but not stiff.",
    task="Convert the following developer notes into a client-ready status update.",
    output_format="""## Weekly Status Update — [Week of Date]

### Progress This Week
- 3-5 bullet points in plain language (no jargon)

### Upcoming
- What's planned for next week

### Risks / Blockers
- Anything the client should know about (or "None — on track")

### Metrics
- Any relevant numbers (tickets closed, features shipped, etc.)""",
    constraints=[
        "Translate technical language into business language",
        "Don't hide problems — but frame them with solutions or next steps",
        "Keep it under 200 words total",
        "No acronyms unless the client uses them too",
    ],
)

print("\n\n" + "=" * 60)
print("All 5 prompts built successfully!")
print("=" * 60)
print("\nPrompts created:")
print("  1. Code Review")
print("  2. Meeting Summary")
print("  3. Requirements Extraction")
print("  4. Bug Report Triage")
print("  5. Status Update")
