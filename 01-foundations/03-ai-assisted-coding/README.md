# AI-Assisted Coding

> Copilot, Claude Code, Cursor — what they're actually good at, what they're bad at, and how to calibrate your trust.

## Prerequisites

- [LLM Fundamentals](../01-llm-fundamentals/) — understanding tokens and hallucinations is critical here
- [Prompt Engineering](../02-prompt-engineering/) — you'll prompt these tools better if you've done the prompt engineering module
- Active experience writing code in any language

## What You'll Learn

- The current landscape of AI coding tools and how they differ architecturally
- What AI coding tools are genuinely good at (and it's a lot)
- What they're reliably bad at (and this list might surprise you)
- How to calibrate your trust — when to accept, verify, or reject AI suggestions
- How to measure whether AI tools are actually making you faster

## The Concept

### The Landscape: What Exists and How It Works

AI coding tools aren't all the same, and understanding the differences matters because each architecture has different strengths and failure modes.

**Autocomplete tools (GitHub Copilot, Codeium, Supermaven)**
These work like aggressive autocomplete on steroids. They see your current file (and sometimes neighboring files), predict what you're about to type, and offer inline suggestions. You accept with Tab, reject by typing something else.

How they work: Your code is sent as context to a model that predicts the next tokens. It's fundamentally the same token prediction from Module 01, just applied to code instead of natural language.

**Chat-based tools (ChatGPT, Claude.ai, Gemini)**
These are the general-purpose LLMs you access through a chat interface. You paste code in, ask questions, get answers back. Copy-paste workflow — the AI doesn't touch your editor directly.

How they work: Same models as autocomplete, but the interface is conversational. You provide context manually (pasting code, describing your setup) and get responses you manually apply.

**Agentic tools (Claude Code, Cursor, Windsurf, Aider)**
These are the newest category and the most powerful. They can read your entire codebase, edit multiple files, run commands, and execute multi-step plans. Instead of suggesting one line, they can implement an entire feature.

How they work: An LLM with tool access — it can read files, write files, run terminal commands, and iterate. It plans, executes, checks its work, and adjusts. This is closest to "pair programming with an AI."

### What AI Coding Tools Are Good At

Let's be concrete. Here are the things where AI tools reliably save time:

**Boilerplate and scaffolding.** Need a new React component with props, a FastAPI endpoint with Pydantic models, or a database migration? AI tools crush this. The patterns are well-established in training data, and there's little ambiguity about what "correct" looks like.

**Language/framework translation.** "Rewrite this Python function in TypeScript" or "Convert this class component to a functional component with hooks" — AI tools handle this surprisingly well because it's mostly pattern transformation.

**Test generation.** Given a function, generating unit tests is one of the highest-value uses. The AI can enumerate edge cases, write assertions, and set up mocks faster than most developers. You'll still need to verify the tests are meaningful, but the scaffolding is solid.

**Code exploration and understanding.** "What does this function do?" and "How does this module work?" — AI tools are excellent at reading code and explaining it in plain language. This is especially valuable when onboarding to an unfamiliar codebase.

**Regex, SQL, and other "write once, read never" code.** Regular expressions, complex SQL queries, shell scripts — these are things most developers Google every time anyway. AI tools are faster and usually more accurate than Stack Overflow for these.

**Documentation.** Generating docstrings, README sections, and inline comments from code. The AI reads the code and describes what it does, which is genuinely useful as a first draft.

### What AI Coding Tools Are Bad At

This is the more important list. These are the failure modes that will cost you time if you don't know about them.

**Novel architecture and design decisions.** AI tools are pattern matchers — they're great when the pattern exists in training data, and unreliable when you need a genuinely novel approach. If you're designing a system architecture, the AI will give you the median Stack Overflow answer, not the right answer for your specific constraints.

**Complex multi-file debugging.** If a bug spans multiple files and requires understanding the interaction between components, AI tools frequently miss the actual cause. They'll suggest fixing symptoms rather than root causes, and they'll confidently suggest changes that have nothing to do with the problem.

**Security-critical code.** Authentication, authorization, encryption, input validation — AI tools will generate code that *looks* secure but has subtle vulnerabilities. SQL injection in AI-generated database code is remarkably common. Never trust AI-generated security code without expert review.

**Performance optimization.** AI tools will suggest optimizations that are technically correct but irrelevant to your actual bottleneck. They optimize what they can see (the code) rather than what matters (the runtime behavior). Profiling first, optimizing second — AI tools skip the first step.

**Knowing when they're wrong.** This is the meta-problem. AI tools don't flag their own uncertainty. A correct suggestion and a subtly broken suggestion look identical — both are presented with equal confidence. The burden of verification is always on you.

### The Trust Calibration Problem

This is the real skill: learning when to trust AI suggestions and when to verify them.

Here's a practical framework:

| Trust Level | When | What to Do |
|-------------|------|------------|
| **Accept immediately** | Boilerplate, simple patterns, obvious completions | Tab and move on |
| **Skim and accept** | Test generation, documentation, format conversions | Quick scan for correctness |
| **Read carefully** | Business logic, data transformations, API integrations | Read every line, run the code |
| **Verify independently** | Security code, financial calculations, anything user-facing | Code review as if a junior wrote it |
| **Write it yourself** | Novel architecture, complex algorithms, critical paths | Use AI for exploration only, not implementation |

The key insight: **treat AI-generated code like code from a very fast but overconfident junior developer.** It's usually close, sometimes brilliant, occasionally dangerously wrong, and never aware of when it's making a mistake.

### Are AI Tools Actually Making You Faster?

This is a genuinely hard question, and the honest answer is: it depends.

**Where the speed-up is real:**
- Greenfield work where you're writing lots of new code from scratch
- Tasks with clear, well-defined patterns (CRUD operations, API integrations)
- Exploring unfamiliar codebases or languages
- Writing tests for existing code

**Where the speed-up is questionable:**
- Debugging (AI often adds investigation time by suggesting wrong fixes)
- Complex refactoring (AI changes might break subtle invariants)
- Tasks that require deep domain knowledge the AI doesn't have

**Where you might actually be slower:**
- Fixing bugs the AI introduced while "helping" with something else
- Over-relying on AI for simple things you could type faster yourself
- Context-switching between reading AI suggestions and your own thinking

The only way to know is to measure. The exercises in this module include a productivity journaling exercise designed to give you actual data on your own experience.

## Why This Matters for Consulting

AI-assisted coding is a multiplier, but only if you know what you're multiplying.

**For client projects:** AI tools can dramatically speed up implementation when the architecture is already decided and the patterns are clear. They're less useful (and potentially harmful) during the design phase when you need to make choices the AI can't evaluate.

**For team management:** If your team is using AI coding tools, you need to know the failure modes so you can adjust your code review process. AI-generated code requires *more* careful review, not less, because the bugs are subtler and the code looks cleaner than it might deserve.

**For client conversations:** "We use AI coding tools" is not a selling point unless you can also articulate your verification process. Clients want to hear that you're using AI to be more efficient, not that you're trusting AI to write their production code unsupervised.

**For staffing and estimation:** AI tools change the equation on developer productivity, but they don't change it as much as the marketing claims suggest. A realistic estimate is 20-40% faster on implementation tasks, near zero improvement on debugging and design tasks, and occasional net-negative on complex tasks where AI suggestions lead you astray.

## Exercises

Head to the [exercises/](exercises/) directory:

| # | Exercise | Description | Est. Time |
|---|----------|-------------|-----------|
| 01 | [Tool Comparison](exercises/starter/01_tool_comparison.md) | Solve the same bug using multiple AI tools, document where each succeeds and fails | 30 min |
| 02 | [Trust Calibration](exercises/starter/02_trust_calibration.py) | Review 10 AI-generated code snippets and identify the ones with subtle bugs | 20 min |
| 03 | [Productivity Journal](exercises/starter/03_productivity_journal.md) | Use an AI coding tool for a real task and log the results | 60+ min |

## Take It Further

- **Read:** [Large Language Models for Software Engineering: A Systematic Literature Review](https://arxiv.org/abs/2308.10620) — academic but practical overview of where AI coding tools actually help
- **Watch:** [Is Copilot Making You a Worse Programmer?](https://www.youtube.com/results?search_query=is+copilot+making+you+worse+programmer) — search for recent takes, this is an active debate
- **Try:** Use a tool you haven't tried before. If you use Copilot, try Claude Code. If you use Claude Code, try Cursor. Each tool has different strengths.
- **Next module:** [Ethics & Liability](../04-ethics-and-liability/) — the rules and responsibilities that come with using AI in consulting work
