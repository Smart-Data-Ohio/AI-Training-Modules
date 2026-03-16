# Exercise 01: Tool Comparison — Solution

## The 3 Bugs

### Bug 1: Pagination Offset

**Problem:** `start = page * page_size` means page 1 starts at index 10 (with default page_size=10), skipping the first 10 items entirely.

**Fix:**
```python
start = (page - 1) * page_size
```

### Bug 2: Case-Insensitive Search

**Problem:** `q.lower() in item["name"]` converts the query to lowercase but doesn't lowercase the item name. Searching for "item" won't match "Item 1".

**Fix:**
```python
results = [item for item in results if q.lower() in item["name"].lower()]
```

### Bug 3: Total Pages Calculation

**Problem:** `len(results) // page_size` uses integer division, which truncates. 25 items with page_size 10 shows 2 total pages instead of 3.

**Fix:**
```python
import math
# ...
"total_pages": math.ceil(len(results) / page_size),
```

## Corrected Code

```python
import math
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

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

    if q:
        results = [item for item in results if q.lower() in item["name"].lower()]

    if category:
        results = [item for item in results if item["category"] == category]

    start = (page - 1) * page_size
    end = start + page_size

    return {
        "items": results[start:end],
        "total": len(results),
        "page": page,
        "page_size": page_size,
        "total_pages": math.ceil(len(results) / page_size) if results else 0,
    }
```

## What to Expect from AI Tools

Most AI tools will find bugs 1 and 3 quickly. Bug 2 is more commonly missed because the code "looks correct" at a glance — the `lower()` call is there, just not in the right place.

Common extra suggestions AI tools might make (not bugs, but improvements):
- Adding type hints to the return value
- Adding error handling for empty results
- Suggesting `total_pages` handle the zero-results edge case
- Recommending offset-based pagination instead of page-based

These are valid suggestions but weren't the exercise. Notice whether your AI tool focused on the actual bugs or got distracted by improvements.
