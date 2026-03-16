"""
Exercise 02: Trust Calibration — Solution
===========================================
See the ANSWERS string in the starter file for detailed explanations.

Quick reference:

    Snippet 1 (Password Validation):  VERIFY — special chars list too narrow
    Snippet 2 (Safe Division):        VERIFY — silent failure, float comparison
    Snippet 3 (Remove Duplicates):    TRUST  — correct and idiomatic
    Snippet 4 (Calculate Discount):   VERIFY — no bounds checking
    Snippet 5 (Read Config):          VERIFY — no error handling, path safety
    Snippet 6 (SQL Sanitization):     REJECT — fundamentally broken approach
    Snippet 7 (Flatten):              TRUST  — clean recursive implementation
    Snippet 8 (Cache Decorator):      VERIFY — no eviction, no kwargs, mutable returns
    Snippet 9 (Parse Date):           VERIFY — no validation, use datetime.strptime
    Snippet 10 (Rate Limiter):        REJECT — Python scoping bug, never works

Key patterns to watch for in AI-generated code:

    1. SECURITY ANTI-PATTERNS (Snippet 6)
       AI loves blocklist-based security. It looks right, sounds right,
       and is completely wrong. Always use the established secure approach
       (parameterized queries, established crypto libraries, etc.)

    2. SCOPING BUGS (Snippet 10)
       AI-generated code frequently creates local variables that shadow
       globals/outer variables. The code runs without errors but doesn't
       do what it's supposed to.

    3. MISSING EDGE CASES (Snippets 4, 9)
       AI generates the happy path well but often misses bounds checking,
       invalid input handling, and edge cases. These are the bugs that
       make it to production.

    4. SILENT FAILURES (Snippets 2, 5)
       Returning a default value instead of raising an error can mask bugs
       downstream. Whether this is acceptable depends on context — but AI
       rarely considers that context.
"""
