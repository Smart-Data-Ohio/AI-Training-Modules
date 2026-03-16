# Prompt Engineering

> Write prompts that produce reliable, useful outputs — not just lucky ones.

## Prerequisites

- [LLM Fundamentals](../01-llm-fundamentals/) (or equivalent understanding of tokens, temperature, and how models generate text)

## What You'll Learn

- How to structure prompts for consistent, high-quality results
- The difference between zero-shot, few-shot, and chain-of-thought prompting
- How system prompts set the stage for everything that follows
- How to get structured output (JSON, markdown, specific formats) reliably
- How to build a reusable prompt library for common consulting tasks

## The Concept

### Why Prompt Structure Matters

Here's something that surprises most developers the first time they hear it: the difference between a mediocre AI output and a great one is usually the prompt, not the model.

You can swap from GPT-4 to Claude to Gemini and get roughly similar results. But change the *prompt* — add structure, give examples, specify the output format — and the quality jump is dramatic. This is why "prompt engineering" is a real skill and not just a buzzword.

The core insight is simple: **LLMs are instruction-following machines, and the quality of the instructions determines the quality of the output.** A vague prompt gets a vague answer. A structured prompt gets a structured answer. It's that straightforward.

### The Anatomy of a Good Prompt

A well-structured prompt has up to five components. You don't always need all five, but knowing the framework lets you add structure when the output isn't good enough.

#### 1. Role

Tell the model who it is. This isn't just flavor text — it genuinely changes the output because it activates different patterns from training data.

```
You are a senior software engineer reviewing code for security vulnerabilities.
```

vs.

```
You are a tech journalist writing for a general audience.
```

Same question, very different answers.

#### 2. Context

Give the model the background it needs. Don't make it guess.

```
We're building a REST API for a healthcare client. The API handles patient
scheduling data. All data must comply with HIPAA requirements.
```

The model can't read your mind or your Jira board. Context fills the gaps.

#### 3. Task

Be explicit about what you want. "Help me with this code" is vague. "Review this function for SQL injection vulnerabilities and suggest fixes" is specific.

The more specific your task, the more useful the output:

| Vague | Specific |
|-------|----------|
| "Help me with this error" | "Explain why this TypeError occurs and show me 2 ways to fix it" |
| "Write some tests" | "Write 3 unit tests for the `calculateDiscount()` function covering edge cases: zero price, negative quantity, and discount > 100%" |
| "Summarize this" | "Summarize this meeting transcript in 3 bullet points, focusing on action items with owners and deadlines" |

#### 4. Format

Tell the model what the output should look like. This is the single highest-leverage thing you can do to get useful output.

```
Respond in the following JSON format:
{
    "severity": "low" | "medium" | "high" | "critical",
    "description": "one-sentence description of the issue",
    "location": "file and line number",
    "fix": "suggested code change"
}
```

Without format instructions, you get a wall of text. With them, you get structured data you can actually parse.

#### 5. Constraints

Tell the model what NOT to do. Constraints are surprisingly effective.

```
- Do not include any code you're not confident is correct
- Keep the summary under 100 words
- Do not mention competitor products by name
- If you're unsure about something, say so explicitly
```

### Few-Shot Prompting: Teaching by Example

Zero-shot prompting is giving the model a task with no examples. Few-shot prompting is giving it a task with examples of what you want.

**Zero-shot:**
```
Classify this customer message as "complaint", "question", or "praise":
"The new dashboard is incredible, saved us hours of work!"
```

**Few-shot (2 examples):**
```
Classify customer messages as "complaint", "question", or "praise".

Examples:
Message: "My order hasn't arrived in 3 weeks"
Category: complaint

Message: "Do you offer volume discounts for teams over 50?"
Category: question

Now classify:
Message: "The new dashboard is incredible, saved us hours of work!"
Category:
```

Few-shot prompting is dramatically more effective for:
- Classification tasks (the model learns your categories from examples)
- Format matching (the model mirrors the structure of your examples)
- Edge cases (your examples define the boundary between categories)

**How many examples do you need?** Usually 2–5. More than that and you're using up context window for diminishing returns. Pick examples that cover the tricky edge cases, not the obvious ones.

### Chain-of-Thought: Making the Model Show Its Work

Chain-of-thought (CoT) prompting asks the model to reason step by step before giving a final answer. It's remarkably effective for anything that requires logic, math, or multi-step reasoning.

**Without CoT:**
```
A store has 15 apples. They sell 8, then receive a shipment of 20.
They give away 5 to employees. How many apples do they have?
```

**With CoT:**
```
A store has 15 apples. They sell 8, then receive a shipment of 20.
They give away 5 to employees. How many apples do they have?

Think through this step by step before giving your answer.
```

That single line — "Think through this step by step" — measurably improves accuracy on reasoning tasks. The model is less likely to skip steps or make arithmetic errors when you force it to show its work.

**When to use CoT:**
- Math or calculations
- Multi-step logic problems
- Code debugging ("trace through this code step by step")
- Complex analysis where you need to see the reasoning

**When NOT to use CoT:**
- Simple factual questions ("What's the capital of France?")
- Creative writing (it'll outline instead of writing)
- Tasks where you don't care about the reasoning, just the answer

### System Prompts: Setting the Stage

System prompts are special instructions that set the model's behavior for an entire conversation. Not all models/APIs support them the same way, but the concept is universal.

A good system prompt establishes:
- **Who** the model is (role, expertise level)
- **How** it should communicate (tone, length, format)
- **What** it should and shouldn't do (capabilities, constraints)

```
You are a senior technical writer at a software consulting company.
You write clear, concise documentation for developer audiences.

Rules:
- Use active voice
- Keep paragraphs to 3 sentences max
- Include code examples for every API endpoint
- Flag any security considerations
- If asked about something outside your expertise, say so
```

System prompts are especially powerful for:
- Building consistent AI features in products (the system prompt is your UI's personality)
- Creating specialized assistants (a code reviewer, a data analyst, a meeting summarizer)
- Enforcing output standards across a team

### Output Formatting: Getting Machine-Readable Results

When you need to parse the output programmatically, format instructions are non-negotiable. Here are the patterns that work:

**JSON output:**
```
Analyze the following code and respond with ONLY valid JSON, no other text:

{
    "language": "detected programming language",
    "complexity": "low | medium | high",
    "issues": [
        {
            "type": "bug | style | performance | security",
            "line": line_number,
            "description": "what's wrong",
            "suggestion": "how to fix it"
        }
    ]
}
```

**Markdown tables:**
```
Compare these three databases and present your analysis as a markdown table
with columns: Feature, PostgreSQL, MongoDB, DynamoDB
```

**Structured sections:**
```
Analyze this PR and respond in exactly this format:

## Summary
One paragraph overview.

## Changes
- Bulleted list of changes

## Concerns
- Any issues found (or "None")

## Verdict
APPROVE, REQUEST_CHANGES, or NEEDS_DISCUSSION
```

**Pro tip:** Including "respond with ONLY [format], no other text" or "do not include any text before or after the JSON" dramatically reduces the chance of the model wrapping its output in chatty preamble.

## Why This Matters for Consulting

Prompt engineering isn't an academic exercise — it's a business differentiator.

**Building a prompt library is building institutional knowledge.** When your team has tested, refined prompts for common tasks (code review, requirements extraction, status reporting), new developers get 80% of the benefit on day one. Clients see consistent quality regardless of which developer is on the project.

**Structured outputs mean you can build on top of AI.** A prompt that returns JSON can feed into dashboards, reports, and automated workflows. A prompt that returns a wall of text requires a human to read it every time. The first approach scales; the second doesn't.

**Knowing prompt patterns saves client money.** Better prompts mean fewer API calls, less back-and-forth, and more first-attempt successes. When you're billing a client for an AI integration, the prompt quality directly affects the cost of every API call their system makes.

Real scenario: A client wants to classify incoming support tickets into categories automatically. A zero-shot prompt gets 70% accuracy. Adding 5 few-shot examples gets it to 92%. Adding a system prompt with category definitions and edge case handling gets it to 97%. Same model, same cost per API call, dramatically different business value — and the only difference is the prompt.

## Exercises

Head to the [exercises/](exercises/) directory:

| # | Exercise | Description | Est. Time |
|---|----------|-------------|-----------|
| 01 | [Prompt Library](exercises/starter/01_prompt_library.py) | Build structured prompts for 5 common consulting tasks | 30 min |
| 02 | [Few-Shot vs Zero-Shot](exercises/starter/02_few_shot_vs_zero_shot.py) | Compare output quality with and without examples | 25 min |
| 03 | [Chain-of-Thought A/B Test](exercises/starter/03_chain_of_thought.py) | Test CoT prompting on reasoning tasks and measure the difference | 25 min |

## Take It Further

- **Read:** [Anthropic's Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) — practical, well-organized, from the team that builds Claude
- **Explore:** [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) — similar quality, GPT-focused
- **Practice:** Take a task you do regularly and write three versions of the prompt at increasing levels of structure. Compare the outputs.
- **Next module:** [AI-Assisted Coding](../03-ai-assisted-coding/) — apply your prompting skills to code-generation tools
