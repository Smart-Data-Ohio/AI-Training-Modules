# Exercise 01: AI Coding Tool Comparison

## The Task

You're going to solve the **same bug** using at least 2 different AI coding tools, then compare the experience.

### The Bug

Here's a Python FastAPI endpoint that's supposed to return paginated search results. It has **3 bugs** — find and fix them all using each tool.

```python
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

# Simulated database
ITEMS = [
    {"id": i, "name": f"Item {i}", "category": cat}
    for i, cat in enumerate(["electronics", "books", "clothing"] * 10)
]


@app.get("/search")
def search_items(
    q: Optional[str] = None,
    category: Optional[str] = None,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1, le=100),
):
    results = ITEMS

    # Filter by search query
    if q:
        results = [item for item in results if q.lower() in item["name"]]

    # Filter by category
    if category:
        results = [item for item in results if item["category"] == category]

    # Paginate
    start = page * page_size
    end = start + page_size

    return {
        "items": results[start:end],
        "total": len(results),
        "page": page,
        "page_size": page_size,
        "total_pages": len(results) // page_size,
    }
```

**Hints:** Think about page 1, items with numeric names, and what happens when total isn't evenly divisible by page_size.

---

## Instructions

### Step 1: Choose Your Tools

Pick at least 2 from this list (or use others):

- [ ] GitHub Copilot (VS Code extension)
- [ ] Claude Code (CLI agent)
- [ ] Cursor (AI-native editor)
- [ ] ChatGPT / Claude.ai (chat interface — paste the code in)
- [ ] Other: _______________

### Step 2: Solve the Bug with Each Tool

For each tool, paste/provide the buggy code and ask it to find and fix the bugs.

**Important:** Use a similar prompt for each tool so you're comparing the tool, not the prompt. Something like:

> "This FastAPI endpoint has 3 bugs. Find and fix all of them. Explain each bug."

### Step 3: Document Your Results

Fill in the comparison table below for each tool:

#### Tool 1: _____________

| Bug | Found? | Fix Correct? | Notes |
|-----|--------|-------------|-------|
| Bug 1 (pagination offset) | | | |
| Bug 2 (search case sensitivity) | | | |
| Bug 3 (total_pages rounding) | | | |

**Time to solution:** ___ minutes
**Did it find all 3?** Yes / No
**Did it find "bugs" that aren't bugs?** Yes / No — describe:
**Quality of explanations:**

#### Tool 2: _____________

| Bug | Found? | Fix Correct? | Notes |
|-----|--------|-------------|-------|
| Bug 1 (pagination offset) | | | |
| Bug 2 (search case sensitivity) | | | |
| Bug 3 (total_pages rounding) | | | |

**Time to solution:** ___ minutes
**Did it find all 3?** Yes / No
**Did it find "bugs" that aren't bugs?** Yes / No — describe:
**Quality of explanations:**

### Step 4: Reflect

Answer these questions:

1. Which tool was fastest to a correct solution?

2. Did any tool find bugs you missed (or suggest improvements beyond the 3 bugs)?

3. Did any tool confidently suggest a "fix" that was actually wrong?

4. How did the experience differ between tools? (e.g., chat vs. inline vs. agentic)

5. Which tool would you use for this kind of task going forward?

---

## The Bugs (Check Your Work)

<details>
<summary>Click to reveal the 3 bugs</summary>

1. **Pagination offset is wrong.** `start = page * page_size` means page 1 starts at index 10 (skips the first 10 items). Should be `start = (page - 1) * page_size`.

2. **Search doesn't match item names properly.** `q.lower() in item["name"]` searches for lowercase query in mixed-case names. `"item"` won't match `"Item 1"` because `item["name"]` isn't lowercased. Should be `q.lower() in item["name"].lower()`.

3. **total_pages uses integer division.** `len(results) // page_size` truncates — 25 items with page_size 10 gives 2 pages instead of 3. Should use `math.ceil(len(results) / page_size)` or `(len(results) + page_size - 1) // page_size`.

</details>
