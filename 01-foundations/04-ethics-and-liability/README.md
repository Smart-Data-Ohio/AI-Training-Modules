# Ethics & Liability

> The stuff that keeps you — and your clients — out of trouble.

## Prerequisites

- [LLM Fundamentals](../01-llm-fundamentals/) — understanding how models work helps you understand why they create risk
- Some exposure to client-facing work (or at least an interest in it)

## What You'll Learn

- What happens to data when you send it to an AI API (and what that means for clients)
- The current legal landscape around AI-generated content and code
- How bias gets into AI systems and what you can do about it
- Your responsibilities as a consultant shipping AI features
- How to draft an AI acceptable use policy for a client engagement

## The Concept

### The Data Question: What Goes In and Where Does It Go?

Every time you send a prompt to an AI API, you're sending data to someone else's server. That's true whether you're using ChatGPT, Claude, GPT-4 via API, or any other hosted model. This is not news to anyone who's worked with cloud services, but AI has some wrinkles that catch people off guard.

**What happens to your data depends on which API you use and how:**

| Method | Data Retention | Training Use | Who Sees It |
|--------|---------------|-------------|-------------|
| Free-tier chat (ChatGPT, Claude.ai) | Stored by default | May be used for training (varies by provider) | Provider's systems, potentially reviewers |
| Paid API (OpenAI, Anthropic, etc.) | Typically not stored long-term | Typically NOT used for training | Provider's systems only during processing |
| Self-hosted / on-premise | You control everything | Never leaves your infrastructure | Only your systems |

**The critical difference:** Most API providers (OpenAI, Anthropic, Google) commit to NOT training on API data in their business terms. But free-tier chat data is a different story — and this is where developers get in trouble, because they prototype in the free chat, then assume the same rules apply.

**What this means for consulting:**

1. **Never paste client code or data into a free-tier chat interface** unless the client has explicitly approved it. This isn't just good practice — depending on your contract, it could be a breach of your NDA.

2. **Read the actual data processing terms** for any AI service you integrate into a client project. "We don't train on your data" and "we delete your data after 30 days" are different claims.

3. **Know the difference between processing and storage.** Even API-based services process your data on their servers. For clients in regulated industries (healthcare, finance, government), processing location and jurisdictional compliance matter.

4. **Document your AI usage in your project's technical documentation.** "We use Anthropic's Claude API for code review assistance; all data is processed under Anthropic's Enterprise API terms, which prohibit training on customer data" is the kind of statement that should exist somewhere in your project docs.

### Client Data + AI: The Rules

There are formal rules (laws, regulations, contracts) and informal rules (professional standards, client expectations). Both matter.

**Formal rules you need to know about:**

- **HIPAA** (Healthcare): Patient data cannot go to an external AI API without a Business Associate Agreement (BAA) and appropriate safeguards. Period. Some providers offer HIPAA-compliant tiers — verify this before building.

- **SOC 2 / SOX** (Finance): If the client's data handling is governed by SOC 2 or Sarbanes-Oxley compliance, adding an AI API to the data flow needs to be evaluated and documented as part of their compliance framework.

- **GDPR / CCPA** (Personal data): If you're processing personal data through an AI API, the provider becomes a data processor under GDPR. You need a Data Processing Agreement (DPA) and the data subject's consent may be required depending on the use case.

- **ITAR / EAR** (Export-controlled): Some government and defense clients have data that can't leave US servers. Most AI APIs process data in multiple regions. This is a hard blocker if it applies.

- **Your NDA / MSA**: Read it. Many consulting contracts have specific provisions about third-party data processing. "We used AI to help" might not be covered by your existing agreement.

**Informal rules that matter just as much:**

- **Tell the client you're using AI.** Transparency isn't just ethical — it's protective. If something goes wrong, "we used AI and told you" is much better than "we used AI and didn't mention it."

- **Don't feed one client's data into a tool while working for another.** Even if the tool doesn't retain data, the optics are terrible and the legal exposure is real.

- **When in doubt, ask.** If you're not sure whether you can send specific data to an AI API, ask your project lead, your client contact, or Smart Data's legal team. The cost of asking is 5 minutes. The cost of guessing wrong is significant.

### IP and Ownership: Who Owns AI-Generated Code?

This is genuinely unsettled law, and it matters for consulting work.

**The current situation (2025–2026):**

- **AI-generated content is probably not copyrightable** in the US. The Copyright Office has ruled that works created by AI without meaningful human involvement can't be copyrighted. This is being tested in courts and may change.

- **AI-assisted content (human + AI collaboration) is murkier.** If a developer uses AI to generate code and then significantly modifies it, the modified version is likely copyrightable by the developer. But where's the line? Nobody knows yet.

- **Code generated by AI might incorporate training data patterns.** This is the GitHub Copilot lawsuit in a nutshell — if the AI was trained on copyleft (GPL) code and generates similar code, is the output derived from the GPL code? Unresolved.

**What this means for consulting:**

1. **Don't ship AI-generated code without human review and modification.** This isn't just about quality — it's about maintaining your claim to authorship.

2. **Document your process.** "Developer wrote the function with AI-assisted autocompletion" is different from "AI generated the entire module from a one-line prompt." If ownership is ever questioned, your process documentation matters.

3. **Check your client contract for AI-specific provisions.** Some clients now have clauses about AI-generated work product. If yours doesn't, consider suggesting one — it protects both sides.

4. **Be especially careful with open-source licenses.** If you're contributing to a client's open-source project, AI-generated code's unclear copyright status could create problems. When in doubt, write it yourself.

### Bias in AI Systems

AI systems can be biased, and if you ship one to a client, that bias becomes your problem.

**How bias gets in:**

1. **Training data bias.** If the training data over-represents certain groups, the model's outputs will too. A language model trained primarily on English internet text will reflect the biases present in English internet text.

2. **Selection bias.** If you fine-tune a model on a dataset of "successful" loan applications, it will learn whatever patterns exist in that historical data — including any discriminatory patterns.

3. **Evaluation bias.** If you test your AI feature only on inputs from one demographic, you won't catch failures that affect other demographics.

4. **Deployment bias.** Even a "fair" model can produce biased outcomes when deployed in a biased context. An AI-powered resume screener might be technically unbiased but deployed in a pipeline that already filters out certain candidates.

**What you can do about it:**

- **Test with diverse inputs.** If you're building a user-facing AI feature, test it with names, languages, and scenarios from different demographics. This is basic QA, not a research project.

- **Monitor outputs.** Once deployed, track whether the AI's outputs show patterns across different user groups. Dashboards and logging aren't just for debugging.

- **Be transparent about limitations.** "This AI tool works best for X and may have reduced accuracy for Y" is honest and responsible. Hiding limitations is how lawsuits happen.

- **Know when NOT to use AI.** Some decisions are too high-stakes for current AI: hiring decisions, lending decisions, criminal justice decisions. Even if the client asks, push back.

### The Consulting Liability Angle

When you ship AI features as a consultant, you're in a unique position:

- **You're the expert.** The client hired you because they don't have AI expertise. If the AI feature has problems, "the AI did it" isn't a defense. You were hired to know better.

- **You're building on someone else's platform.** If the AI provider changes their model, your feature might break or behave differently. Build monitoring and fallbacks.

- **You're responsible for what you deliver.** If an AI-generated code snippet introduces a security vulnerability and the client gets breached, the liability chain includes you — you reviewed and shipped that code.

**The professional standard is straightforward:**

1. Treat AI as a tool, not a colleague. Tools don't make decisions — you do.
2. Review everything. If it ships under your name, you own it.
3. Be transparent about AI usage. Surprises are bad in consulting.
4. Build in guardrails. Rate limiting, content filtering, human-in-the-loop for high-stakes decisions.
5. Document your verification process. If something goes wrong, your documentation is your defense.

## Why This Matters for Consulting

Ethics isn't a separate skill from consulting — it's the foundation of it. Every concept in this module maps to a real scenario you'll face: a client asking you to "just plug their data into ChatGPT," a teammate pasting proprietary code into a free-tier chat, a stakeholder who doesn't understand why the AI feature needs a human review step. Your ability to navigate these conversations — clearly, confidently, without being preachy — is what separates a trusted advisor from a commodity vendor.

**The upside of getting this right** is significant. Clients who trust you to handle AI responsibly will give you more AI work. Smart Data's reputation as a firm that does AI right — not just AI fast — is a competitive advantage.

**The downside of getting this wrong** is severe. A PII leak through an AI tool, a biased AI feature in production, or an IP dispute over AI-generated code — any of these can damage a client relationship, trigger legal action, and harm Smart Data's reputation.

**The good news:** most of this is just applying existing professional standards (data handling, code review, client communication) to a new tool. You already know how to handle client data responsibly. You already know to review code before shipping it. AI doesn't change the principles — it adds new places where the principles apply.

## Exercises

Head to the [exercises/](exercises/) directory:

| # | Exercise | Description | Est. Time |
|---|----------|-------------|-----------|
| 01 | [PII Audit](exercises/starter/01_pii_audit.py) | Identify PII leakage risks in sample prompts and rewrite them safely | 25 min |
| 02 | [AI Data Policy Draft](exercises/starter/02_ai_data_policy.md) | Draft a client-facing AI acceptable use policy | 30 min |

## Take It Further

- **Read:** [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — the security risks specific to AI applications
- **Read:** [Anthropic's Responsible Scaling Policy](https://www.anthropic.com/research/responsible-scaling-policy) — how one AI company thinks about safety
- **Explore:** [AI Incident Database](https://incidentdatabase.ai/) — real cases where AI went wrong
- **Next tier:** [Applied](../../02-applied/) — start building real things with these guardrails in mind
