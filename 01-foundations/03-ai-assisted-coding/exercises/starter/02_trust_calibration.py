"""
Exercise 02: Trust Calibration
================================
Review 10 AI-generated code snippets. Some are correct, some have
subtle bugs. Your job is to identify which ones you'd trust in production.

Objectives:
    1. Practice reading AI-generated code critically
    2. Build instincts for the kinds of bugs AI introduces
    3. Learn to slow down on code that "looks right"

Why this matters:
    In a consulting context, AI-generated code goes through your name
    before it reaches the client. If it ships with a subtle bug, that's
    your bug now. This exercise trains the verification muscle.

Instructions:
    For each snippet, decide: TRUST (ship it), VERIFY (needs changes),
    or REJECT (rewrite it). Then check your answers at the bottom.
"""

# =============================================================================
# Snippet 1: Password Validation
# =============================================================================

def validate_password(password: str) -> bool:
    """Check if password meets security requirements."""
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)
    return has_upper and has_lower and has_digit and has_special

# Your verdict: TRUST / VERIFY / REJECT
# Why:


# =============================================================================
# Snippet 2: Safe Division
# =============================================================================

def safe_divide(a: float, b: float) -> float:
    """Safely divide two numbers, returning 0 if divisor is zero."""
    if b == 0:
        return 0
    return a / b

# Your verdict: TRUST / VERIFY / REJECT
# Why:


# =============================================================================
# Snippet 3: Remove Duplicates Preserving Order
# =============================================================================

def remove_duplicates(items: list) -> list:
    """Remove duplicates from a list while preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Your verdict: TRUST / VERIFY / REJECT
# Why:


# =============================================================================
# Snippet 4: Calculate Discount
# =============================================================================

def calculate_discount(price: float, discount_percent: float) -> float:
    """Apply a percentage discount to a price."""
    discount = price * discount_percent / 100
    return price - discount

# Your verdict: TRUST / VERIFY / REJECT
# Why:


# =============================================================================
# Snippet 5: Read Config File
# =============================================================================

import json

def read_config(filepath: str) -> dict:
    """Read a JSON config file and return its contents."""
    with open(filepath) as f:
        config = json.load(f)
    return config

# Your verdict: TRUST / VERIFY / REJECT
# Why:


# =============================================================================
# Snippet 6: Sanitize User Input for SQL
# =============================================================================

def sanitize_for_sql(user_input: str) -> str:
    """Sanitize user input to prevent SQL injection."""
    dangerous_chars = ["'", '"', ";", "--", "/*", "*/", "DROP", "DELETE"]
    result = user_input
    for char in dangerous_chars:
        result = result.replace(char, "")
    return result

# Your verdict: TRUST / VERIFY / REJECT
# Why:


# =============================================================================
# Snippet 7: Flatten Nested List
# =============================================================================

def flatten(nested_list: list) -> list:
    """Flatten a nested list of arbitrary depth."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Your verdict: TRUST / VERIFY / REJECT
# Why:


# =============================================================================
# Snippet 8: Cache Decorator
# =============================================================================

def cache(func):
    """Simple caching decorator for function results."""
    _cache = {}
    def wrapper(*args):
        if args not in _cache:
            _cache[args] = func(*args)
        return _cache[args]
    return wrapper

# Your verdict: TRUST / VERIFY / REJECT
# Why:


# =============================================================================
# Snippet 9: Parse Date String
# =============================================================================

def parse_date(date_str: str) -> tuple[int, int, int]:
    """Parse a date string in YYYY-MM-DD format."""
    parts = date_str.split("-")
    return int(parts[0]), int(parts[1]), int(parts[2])

# Your verdict: TRUST / VERIFY / REJECT
# Why:


# =============================================================================
# Snippet 10: Rate Limiter Check
# =============================================================================

import time

request_log = []

def is_rate_limited(max_requests: int = 100, window_seconds: int = 60) -> bool:
    """Check if the current request exceeds the rate limit."""
    now = time.time()
    # Remove old entries
    request_log = [t for t in request_log if now - t < window_seconds]
    # Check limit
    if len(request_log) >= max_requests:
        return True
    request_log.append(now)
    return False

# Your verdict: TRUST / VERIFY / REJECT
# Why:


# =============================================================================
# CHECK YOUR ANSWERS BELOW
# (Don't peek until you've made your verdicts!)
# =============================================================================

ANSWERS = """

---------------------------------------------------------------
ANSWERS — scroll down
---------------------------------------------------------------
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.

Snippet 1 (Password Validation): VERIFY
    The logic works, but the special character set is incomplete.
    What about ()_+-=[]{}|\\:";'<>?,./ and other special chars?
    Also, no maximum length check (some systems need one).
    Not a bug, but worth expanding before shipping.

Snippet 2 (Safe Division): VERIFY
    Returning 0 for division by zero is a silent failure.
    Is that what the caller expects? In many cases, returning None
    or raising a specific exception is safer. Also, comparing floats
    with == is risky — b could be 0.0000000001 and cause issues.
    Context-dependent, so: verify with the team.

Snippet 3 (Remove Duplicates): TRUST
    This is correct and idiomatic. Works for hashable items.
    Would fail for unhashable items (lists, dicts) in the set, but
    that's a reasonable limitation. Ship it.

Snippet 4 (Calculate Discount): VERIFY
    Works mathematically, but no input validation. What if
    discount_percent is 150? You'd get a negative price.
    What if price is negative? Depends on context whether this
    matters, but for a client-facing app, add bounds checking.

Snippet 5 (Read Config): VERIFY
    Works but has no error handling. What if the file doesn't exist?
    What if it's not valid JSON? In production you'd want try/except
    with useful error messages. Also: no path validation — could
    read any file on the system if filepath comes from user input.

Snippet 6 (SQL Sanitization): REJECT ⚠️
    THIS IS THE DANGEROUS ONE. Blocklist-based SQL sanitization is
    fundamentally broken. It misses countless injection vectors
    (UNION, OR 1=1, hex encoding, etc.). The only correct approach
    is parameterized queries / prepared statements. This function
    gives a false sense of security. Never ship this.

Snippet 7 (Flatten): TRUST
    Clean recursive implementation. Works correctly for nested lists
    of arbitrary depth. Could hit recursion limits on extremely deep
    nesting, but that's an edge case. Ship it.

Snippet 8 (Cache Decorator): VERIFY
    Works for hashable args, but: no cache eviction (memory leak
    over time), doesn't handle kwargs, and mutable return values
    could be modified by callers. For production, use
    functools.lru_cache instead. Fine for quick scripts.

Snippet 9 (Parse Date): VERIFY
    Works for valid YYYY-MM-DD input but has zero validation.
    "not-a-date" would crash. "2024-13-45" would return invalid
    month/day without complaint. Use datetime.strptime() instead
    for production code.

Snippet 10 (Rate Limiter): REJECT ⚠️
    Has a Python scoping bug! The line
        request_log = [t for t in request_log if ...]
    creates a LOCAL variable that shadows the global request_log.
    The function never actually modifies the global list, so it
    never records requests and never rate-limits anyone.
    Would need `global request_log` or a different data structure.
    Also: not thread-safe, uses a global list (won't work across
    processes). Use a proper rate limiter library in production.

SCORING:
  8-10 correct: Excellent trust calibration
  6-7 correct:  Good instincts, keep practicing
  4-5 correct:  Review the ones you missed — common AI patterns
  <4 correct:   Re-read the LLM Fundamentals module on hallucinations
"""

# Uncomment to see answers:
# print(ANSWERS)
