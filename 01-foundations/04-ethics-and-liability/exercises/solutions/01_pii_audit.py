"""
Exercise 01: PII Audit — Solution
====================================
"""

# =============================================================================
# Prompt 1: Code Review Request
# =============================================================================

prompt_1_pii = [
    "Client name: 'Acme Corp' (if under NDA)",
    "Developer name: 'John Smith'",
    "Healthcare context: 'Cleveland Clinic deployment' (reveals client + industry)",
    "SSN handling visible in code (reveals data schema)",
    "Database column names (reveals internal architecture)",
    "Specific clinic identifier: 'cleveland_main'",
]

prompt_1_risk = "critical"
# Why: Healthcare data + SSN + named client + named developer.
# If this prompt goes to an AI API, you've disclosed a client relationship,
# a developer's identity, and the fact that you're handling SSNs for a
# healthcare deployment. Under HIPAA, this is a serious concern.

prompt_1_rewritten = """
Review this function that handles record intake for a healthcare application.
The code processes sensitive identifiers and personal information:

def process_intake(identifier, name, date_of_birth):
    record = db.query(f"SELECT * FROM records WHERE id='{identifier}'")
    if not record:
        db.insert("records", {
            "id": identifier,
            "name": name,
            "dob": date_of_birth,
            "location": "primary_location"
        })
    return record

I'm concerned about the SQL query construction and the overall
approach to handling sensitive data. What issues do you see?
"""


# =============================================================================
# Prompt 2: Data Analysis Request
# =============================================================================

prompt_2_pii = [
    "Full names: Sarah Johnson, Mike Chen, Priya Patel, James Williams",
    "Email addresses: sjohnson@gmail.com, mchen@techcorp.com, etc.",
    "Company affiliations via email domains (techcorp.com, bigbank.com)",
    "Individual spending amounts linked to named people",
    "Login dates linked to named people (behavioral data)",
]

prompt_2_risk = "high"
# Why: Named individuals with spending data and email addresses.
# Even without explicit financial account numbers, this is enough
# to identify and profile specific people.

prompt_2_rewritten = """
Analyze this anonymized customer data and identify churn patterns:

Customer ID, Last Login, Monthly Spend
CUST-001, 2025-01-15, $299
CUST-002, 2024-11-03, $599
CUST-003, 2025-02-28, $149
CUST-004, 2024-09-12, $899

What patterns suggest a customer is likely to churn?
"""


# =============================================================================
# Prompt 3: Bug Report Analysis
# =============================================================================

prompt_3_pii = [
    "IP address: 192.168.1.42",
    "Email/account: admin@smartdata.com (reveals company + admin access)",
    "Customer name: David Lee",
    "Customer ID: CUST-5521",
    "Order number: ORD-789456",
    "Partial card number: ending 4242",
    "Transaction amount: $1,247.50 (linked to named customer)",
    "Company name: SmartData Ohio LLC (as merchant)",
]

prompt_3_risk = "critical"
# Why: Payment card data (even partial) + named customer + transaction amount.
# This could violate PCI-DSS requirements. The IP address and admin account
# also reveal internal infrastructure.

prompt_3_rewritten = """
Help me debug a payment processing timeout. The error log shows:

ERROR [timestamp] - Failed to process payment for order
  Error: Payment API timeout after 30s
  Payment provider: Stripe
  Context: API call timed out during charge creation

The payment amount and customer details aren't relevant to the
timeout issue. What are common causes for Stripe API timeouts
and how should I handle them?
"""


# =============================================================================
# Prompt 4: Resume Screening
# =============================================================================

prompt_4_pii = [
    "Full names: Maria Garcia, Robert Kim",
    "Ages: 34, 28 (age discrimination risk)",
    "Universities: Ohio State, MIT",
    "Previous employers: Google, unnamed startup",
    "Home cities: Columbus OH, San Francisco CA",
    "Salary expectations: $145k, $185k",
    "Graduation years (can be used to infer age)",
    "Gender (inferable from names)",
    "Ethnicity (inferable from names)",
]

prompt_4_risk = "critical"
# Why: This is a hiring decision with enough PII to identify both candidates.
# Using AI for hiring decisions with this much identifying information creates
# discrimination risk. The ages, names (gender/ethnicity inference), and
# locations could all contribute to biased AI recommendations.
# Additionally, salary information is confidential in most contexts.

prompt_4_rewritten = """
Compare two candidates for a Senior Developer position based on
qualifications only:

Candidate A:
- B.S. Computer Science
- 12 years total experience
- 10 years at a large tech company, 2 years freelancing
- Strengths: stability, deep experience

Candidate B:
- M.S. Machine Learning
- 4 years total experience
- Held CTO title at a startup
- Strengths: leadership experience, ML specialization

The role requires: [specific requirements here]

Based on qualifications and role fit, what are the tradeoffs
between these candidates?

NOTE: I've intentionally removed identifying information. I'll
make the final hiring decision based on the full picture.
"""


# =============================================================================
# Prompt 5: The "Seems Fine" Prompt
# =============================================================================

prompt_5_pii = [
    "Internal hostname: db.internal.smartdata.com",
    "Database port: 5432",
    "Service account username: svc_analytics",
    "PASSWORD IN PLAINTEXT: Sm@rtD4ta2025!",
    "Company infrastructure details",
]

prompt_5_risk = "critical"
# Why: PLAINTEXT CREDENTIALS sent to an external API. This is the worst one.
# The password is now potentially stored in the AI provider's logs.
# The internal hostname reveals infrastructure. Combined, this is
# enough for an attacker to access the database.
# This password should be rotated IMMEDIATELY if this prompt was
# actually sent to an AI service.

prompt_5_rewritten = """
Write a Python function that connects to a PostgreSQL database
using credentials loaded from environment variables and runs
a health check query. Use psycopg2 or sqlalchemy.

The function should:
- Read DB_HOST, DB_PORT, DB_USER, DB_PASSWORD from environment variables
- Run a simple SELECT 1 query
- Return True if successful, False otherwise
- Handle connection timeouts gracefully
"""


# =============================================================================
# Summary
# =============================================================================

summary = """
PII Audit Summary
===================

1. Which prompt had the highest risk? Why?
   Prompt 5 (credentials) and Prompt 3 (payment data) are tied for
   highest risk. Prompt 5 is arguably worse because it provides direct
   access to infrastructure, while Prompt 3 exposes transaction data
   for a specific person.

2. Which PII was hardest to spot?
   - Email domains revealing company affiliations (Prompt 2)
   - Age/ethnicity inference from names and graduation years (Prompt 4)
   - The internal hostname revealing infrastructure (Prompt 5 — most
     people notice the password but not the hostname)

3. Rule of thumb for "is this safe to send to an AI API"?
   Before sending any prompt, scan for:
   (a) Names — of people, companies, or internal systems
   (b) Numbers — IDs, accounts, amounts, addresses
   (c) Credentials — passwords, keys, tokens, internal URLs
   (d) Context — could someone reconstruct who/what this is about?
   If any of these are present, anonymize or remove them first.

4. How would you train a team to avoid these mistakes?
   - Make PII review a checklist item before any AI API call
   - Share examples like these in onboarding
   - Create a pre-prompt review tool or linter if possible
   - Establish a culture where it's OK to ask "is this safe to send?"
"""

print(summary)
