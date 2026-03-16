# Exercise 02: AI Data Policy — Solution

This is a completed example policy. Your version should reflect the specific project context, but this shows the level of detail and specificity to aim for.

---

# AI Acceptable Use Policy

**Project:** Customer Insights Dashboard
**Client:** Meridian Financial Services (fictional)
**Prepared by:** Smart Data Ohio
**Date:** March 2026

## 1. Purpose

This policy defines how AI tools and services will be used during the Customer Insights Dashboard project. It establishes data handling boundaries, review processes, and security requirements to protect Meridian's customer data and maintain SOC 2 compliance. Both Smart Data and Meridian are bound by this policy for the duration of the engagement.

## 2. AI Tools in Use

| Tool | Purpose | Data Exposure | Provider Terms |
|------|---------|--------------|----------------|
| Anthropic Claude API (Enterprise) | Natural language search, report summarization | Anonymized query patterns, aggregated financial summaries only | Enterprise terms: no data retention, no training, SOC 2 Type II certified |
| GitHub Copilot Business | Developer code assistance | Code snippets only — no customer data in prompts | Business terms: no code retention, no training on business tier |
| Internal embedding model (self-hosted) | Document search index | Customer-facing documents (already public/semi-public) | Self-hosted — no external data transfer |

## 3. Data Handling Rules

### 3.1 Data That May Be Processed by AI Tools

- Aggregated, anonymized financial summaries (no individual customer data)
- Publicly available market data and reports
- Internal documentation and knowledge base articles
- Code written for this project (via Copilot, no customer data in code comments)
- Sample/synthetic data for testing and development

### 3.2 Data That Must NEVER Be Sent to AI Tools

- Individual customer names, account numbers, or SSNs
- Transaction-level financial data
- Customer contact information (email, phone, address)
- Authentication credentials, API keys, or internal hostnames
- Meridian's proprietary financial models or algorithms
- Any data subject to SOC 2 access controls

### 3.3 Data Anonymization Requirements

When data must be processed by AI tools for development or testing:
- Replace customer names with synthetic names using Faker library
- Replace account numbers with randomly generated equivalents
- Aggregate financial data to cohort level (minimum 50 customers per group)
- Remove all timestamps more specific than month/year
- Use the project's anonymization script (`scripts/anonymize.py`) for consistency

## 4. Code and Content Review Standards

### 4.1 AI-Generated Code

All code written with AI assistance must:
- Pass standard code review by a human developer who did NOT use AI for the same section
- Pass automated security scanning (Snyk/Semgrep) before merge
- Include a comment indicating AI assistance was used (for audit purposes)
- Be tested with the same rigor as hand-written code (unit + integration tests required)

### 4.2 AI-Generated Content

User-facing text generated or summarized by AI must:
- Be reviewed by the project lead before deployment
- Include accuracy verification against source data
- Be labeled with a disclosure indicator in the UI ("AI-generated summary")
- Have a feedback mechanism for end users to flag inaccuracies

## 5. Security Requirements

- API keys stored in environment variables or secrets manager — never in code or prompts
- All AI API calls logged with timestamp, user, and prompt hash (not prompt content) for audit trail
- AI service access restricted to project team members via role-based access control
- Monthly review of AI API usage logs for anomalies
- Encryption in transit (TLS 1.2+) for all AI API communications
- No AI tool access from personal devices — project VPN required

## 6. Bias and Fairness

- Quarterly review of AI-generated search results and summaries for demographic bias
- Dashboard analytics broken down by customer segment to identify disparate impact
- Fair lending compliance check before any AI feature that influences customer-facing decisions
- Documented testing with diverse customer profiles before feature launch
- Escalation path: any team member can flag a potential bias concern to the project lead

## 7. Incident Response

**AI-specific incidents include:** data leak through AI tool, biased output reaching customers, incorrect financial information in AI-generated reports.

**Response timeline:**
1. **0–1 hour:** Disable affected AI feature, notify project lead and Meridian's IT security contact
2. **1–4 hours:** Assess scope, preserve logs, determine root cause
3. **4–24 hours:** Written incident report to Meridian's project sponsor
4. **1 week:** Remediation plan with timeline
5. **Post-incident:** Policy review and update

**Notification chain:** Developer → Project Lead → Smart Data Account Manager → Meridian IT Security → Meridian Project Sponsor

## 8. Transparency

- All AI-generated content in the dashboard is labeled with a subtle indicator
- The dashboard's "About" section includes a statement about AI usage
- Meridian's privacy policy will be updated to reflect AI-assisted data processing
- End users can opt out of AI-generated summaries and see raw data instead

## 9. Training Requirements

Before using AI tools on this project, team members must:
- Read this policy in full (acknowledge via email)
- Complete Smart Data's AI Foundations training (Modules 01 and 04 at minimum)
- Review the project-specific data classification guide
- Pass a 10-question quiz on data handling rules (maintained by project lead)

New team members have 1 week to complete training; no AI tool access until completed.

## 10. Policy Review

- Reviewed quarterly or after any AI-related incident (whichever is sooner)
- Smart Data project lead owns updates; Meridian IT security reviews and approves
- Changes communicated via team email + discussed in next project standup
- Version history maintained in project documentation repository
