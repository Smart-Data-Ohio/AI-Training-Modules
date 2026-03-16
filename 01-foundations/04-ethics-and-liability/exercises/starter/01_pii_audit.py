"""
Exercise 01: PII Audit
========================
Review sample prompts for PII leakage risks and rewrite them safely.

Objectives:
    1. Identify Personally Identifiable Information (PII) in AI prompts
    2. Understand why PII in prompts is a risk
    3. Practice rewriting prompts to remove PII while preserving utility

Why this matters:
    In consulting, one careless prompt with client data can violate NDAs,
    breach regulations, and destroy trust. This exercise builds the habit
    of scanning prompts before sending them.

Instructions:
    For each prompt below:
    1. Identify ALL PII present
    2. Rate the risk level (low / medium / high / critical)
    3. Rewrite the prompt to remove PII while keeping it useful
"""


# =============================================================================
# PII Categories Reference
# =============================================================================
#
# Direct PII (identifies a specific person):
#   - Full name, email, phone number
#   - Social Security Number, driver's license
#   - Medical record numbers, patient IDs
#   - Financial account numbers
#   - Home address
#
# Indirect PII (can identify when combined):
#   - Date of birth, age
#   - Job title + company (small company = identifiable)
#   - IP addresses, device identifiers
#   - Location data
#
# Business-Sensitive (not PII but still risky):
#   - Internal project names / code names
#   - Client company names (if under NDA)
#   - Revenue figures, pricing
#   - Internal URLs, API keys


# =============================================================================
# Prompt 1: Code Review Request
# =============================================================================

prompt_1 = """
Review this function from our Acme Corp project. John Smith wrote it
and it handles patient intake for their Cleveland Clinic deployment:

def process_intake(patient_ssn, patient_name, dob):
    record = db.query(f"SELECT * FROM patients WHERE ssn='{patient_ssn}'")
    if not record:
        db.insert("patients", {
            "ssn": patient_ssn,
            "name": patient_name,
            "dob": dob,
            "clinic": "cleveland_main"
        })
    return record
"""

# TODO: What PII/sensitive data is in this prompt?
prompt_1_pii = []  # TODO: List each piece of PII or sensitive data as strings

# TODO: Rate the risk level
prompt_1_risk = ""  # low / medium / high / critical

# TODO: Rewrite the prompt to remove PII while keeping it useful
prompt_1_rewritten = """
TODO: Rewrite prompt_1 here
"""


# =============================================================================
# Prompt 2: Data Analysis Request
# =============================================================================

prompt_2 = """
Analyze this customer data and identify churn patterns:

Name, Email, Last Login, Monthly Spend
Sarah Johnson, sjohnson@gmail.com, 2025-01-15, $299
Mike Chen, mchen@techcorp.com, 2024-11-03, $599
Priya Patel, ppatel@yahoo.com, 2025-02-28, $149
James Williams, jwilliams@bigbank.com, 2024-09-12, $899
"""

# TODO: What PII is in this prompt?
prompt_2_pii = []
prompt_2_risk = ""
prompt_2_rewritten = """
TODO: Rewrite prompt_2 here
"""


# =============================================================================
# Prompt 3: Bug Report Analysis
# =============================================================================

prompt_3 = """
Help me debug this error. The user reported it from IP 192.168.1.42
using the account admin@smartdata.com. The error log shows:

ERROR 2025-03-15 14:23:01 - Failed to process payment for order #ORD-789456
  Customer: David Lee (customer_id: CUST-5521)
  Card ending: 4242
  Amount: $1,247.50
  Merchant: SmartData Ohio LLC
  Error: Stripe API timeout after 30s
"""

# TODO: What PII is in this prompt?
prompt_3_pii = []
prompt_3_risk = ""
prompt_3_rewritten = """
TODO: Rewrite prompt_3 here
"""


# =============================================================================
# Prompt 4: Resume Screening
# =============================================================================

prompt_4 = """
Compare these two candidates for the Senior Developer position:

Candidate A: Maria Garcia, 34, graduated Ohio State 2014.
B.S. Computer Science. 10 years at Google, then 2 years freelancing.
Lives in Columbus, OH. Asking $145k.

Candidate B: Robert Kim, 28, graduated MIT 2020.
M.S. Machine Learning. 4 years at startup (CTO).
Lives in San Francisco, CA. Asking $185k.

Which candidate is a better fit?
"""

# TODO: What PII is in this prompt?
prompt_4_pii = []
prompt_4_risk = ""
prompt_4_rewritten = """
TODO: Rewrite prompt_4 here
"""


# =============================================================================
# Prompt 5: The "Seems Fine" Prompt
# NOTE: The credentials below are FICTIONAL — used for training purposes only.
# =============================================================================

prompt_5 = """
Write a Python function that connects to our database at
db.internal.smartdata.com:5432 using the service account
credentials (username: svc_analytics, password: Sm@rtD4ta2025!)
and runs a health check query.
"""

# TODO: What sensitive data is in this prompt?
prompt_5_pii = []
prompt_5_risk = ""
prompt_5_rewritten = """
TODO: Rewrite prompt_5 here
"""


# =============================================================================
# Summary
# =============================================================================

# TODO: After completing all 5 audits, answer these questions:

summary = """
PII Audit Summary
===================

1. Which prompt had the highest risk? Why?


2. Which PII was hardest to spot? (i.e., what did you almost miss?)


3. What's your rule of thumb for "is this safe to send to an AI API"?


4. How would you train a team to avoid these mistakes?

"""

# TODO: Print your completed summary
# print(summary)
