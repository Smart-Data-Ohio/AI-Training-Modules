# LLM Fundamentals

> Understand how language models actually work so you can make smart decisions about when and how to use them.

## Prerequisites

- Basic programming experience (any language)
- You've used ChatGPT, Claude, or a similar tool at least casually

## What You'll Learn

- What tokens are and why they control everything (cost, speed, behavior)
- How context windows work and why they matter for real applications
- What temperature does and how to use it intentionally
- What embeddings are and why they're the secret weapon behind search and RAG
- Why models hallucinate — and why it's not a bug

## The Concept

### Tokens: The Atoms of Language Models

Here's the first thing most people get wrong about LLMs: they don't read words. They read **tokens**.

A token is a chunk of text — sometimes a whole word, sometimes part of a word, sometimes just a character. The word "hamburger" becomes three tokens: `ham`, `burger`... just kidding. It's actually `ham`, `bur`, `ger`. The word "the" is one token. A newline character is one token. The number "123456789" might be multiple tokens.

Why does this matter? Three reasons:

1. **Cost.** API pricing is per-token. If you're sending a 10-page document to Claude or GPT, you're paying for every token in that document — plus every token in the response. Understanding tokenization helps you estimate costs before you build.

2. **Limits.** Every model has a maximum number of tokens it can handle (the context window — more on that next). If you don't know how your input tokenizes, you can't predict when you'll hit the wall.

3. **Behavior.** Models process tokens, not words. This is why they're weirdly bad at counting letters in words or reversing strings — the model literally doesn't see individual characters the way you do.

**The practical takeaway:** When you're estimating costs or planning what to send to an API, remember that 1 token ≈ 4 characters in English, or roughly ¾ of a word. A typical page of text is about 300-400 tokens.

### Context Windows: How Much the Model Can "See"

The context window is the total number of tokens a model can process in a single request — your input _and_ the output combined.

Think of it like the model's working memory. When you're having a conversation with Claude and it "remembers" what you said earlier, it's not actually remembering anything — the entire conversation history is being sent as input every time. When that conversation gets too long and exceeds the context window, older messages get dropped, and the model genuinely has no idea what you talked about.

Here's what context windows look like in practice (these shift frequently — check the provider's docs for current numbers):

| Model            | Context Window |
|------------------|----------------|
| GPT-4o           | 128K tokens    |
| Claude Sonnet 4  | 200K tokens    |
| Claude Opus 4    | 200K tokens    |
| Gemini 2.0 Pro   | 1M–2M tokens   |

These numbers sound huge, but they fill up fast:

- A 50-page contract? ~15,000 tokens.
- An entire codebase? You might blow through 200K tokens before you've loaded all the files.
- A 2-hour meeting transcript? Easily 20,000+ tokens.

**Why this matters for consulting:** When a client says "can we just feed our whole knowledge base into the AI?", your context window knowledge tells you whether that's feasible, what it'll cost, and what the alternatives are (spoiler: this is where RAG comes in — covered in the Applied tier).

### Temperature: Creativity vs. Consistency

Temperature is a number (usually 0 to 1, sometimes up to 2) that controls how "random" the model's output is.

Here's the intuition: at every step of generating a response, the model is choosing the next token from a probability distribution. Temperature adjusts that distribution:

- **Temperature 0:** The model always picks the most probable next token. Deterministic, consistent, boring. Use this for tasks where you want the same answer every time — code generation, data extraction, classification.
- **Temperature 0.7:** The model sometimes picks less probable tokens. More varied, more creative, occasionally surprising. Good for writing, brainstorming, and creative tasks.
- **Temperature 1.0+:** The model frequently picks improbable tokens. Chaotic, unpredictable, sometimes nonsensical. Rarely what you want in production.

**The analogy:** Temperature 0 is a GPS giving you turn-by-turn directions. Temperature 1 is a friend who says "I know a shortcut" and maybe takes you somewhere amazing, maybe gets you lost.

**The practical rule:** Start at 0 for anything that needs to be reliable. Only turn it up when you explicitly want variety. Most production applications live between 0 and 0.3.

### Embeddings: Meaning as Numbers

This one's a bit more abstract, but it's arguably the most powerful concept in this module.

An embedding is a list of numbers (a vector) that represents the _meaning_ of a piece of text. The word "dog" might become something like `[0.2, -0.5, 0.8, ...]` — a vector with hundreds or thousands of dimensions.

The magic: texts with similar meanings end up close together in this number space. "Golden retriever" and "Labrador" have similar embeddings. "Golden retriever" and "quantum mechanics" don't.

Why should you care? Because embeddings are how you make AI **search** work. Instead of matching keywords (old-school search), you can:

1. Turn your documents into embeddings
2. Turn the user's question into an embedding
3. Find the documents whose embeddings are closest to the question's embedding
4. Feed those documents to the LLM as context

This is the core of **Retrieval-Augmented Generation (RAG)** — the pattern you'll build in the Applied tier. For now, just understand the concept: embeddings turn meaning into math, and that math lets you find relevant information at scale.

**The analogy:** Imagine you could place every book in a library on a giant map, where books about similar topics are physically close together. When someone asks a question, you find the spot on the map where that question would live, and grab the nearest books. That's embeddings.

### Why Models Hallucinate

Here's the uncomfortable truth: hallucination isn't a bug in LLMs. It's a feature — or at least, a direct consequence of how they work.

An LLM is a next-token prediction machine. Given a sequence of tokens, it predicts what token is most likely to come next. It does this incredibly well because it was trained on a massive amount of text. But here's the key insight:

**The model doesn't know what's true. It knows what sounds right.**

When you ask "Who invented the telephone?", the model doesn't look up the answer in a database. It generates the tokens that are statistically most likely to follow that question based on its training data. Usually that produces "Alexander Graham Bell" — which happens to be correct (or at least the commonly accepted answer). But the model arrived at that answer through pattern matching, not knowledge retrieval.

This breaks down when:

- **The model hasn't seen enough examples** — ask about obscure topics and it'll generate plausible-sounding nonsense
- **The question has a confident-sounding wrong answer** — the model might produce it because it sounds right
- **You ask for specific facts** (dates, URLs, citations) — the model generates things that _look like_ dates, URLs, and citations, whether or not they're real

**The practical takeaway:** Never trust an LLM for factual claims without verification. Use them to _draft_, _analyze_, _transform_, and _reason_ — not as a source of truth. In a consulting context, this means you always verify AI-generated content before it goes to a client.

**Common hallucination patterns to watch for:**

- Fabricated citations and URLs (very common)
- Confident but wrong dates and statistics
- Plausible-sounding technical details that don't exist
- "Averaging" multiple real things into a fictional composite

## Why This Matters for Consulting

Every concept in this module maps directly to consulting conversations:

| Concept             | Consulting Application                                                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Tokens**          | Estimating API costs for a client proposal. "This feature will process ~X tokens per request at $Y per million tokens."        |
| **Context windows** | Scoping what's feasible. "We can't feed your entire knowledge base into one prompt, but here's what we _can_ do."              |
| **Temperature**     | Setting expectations. "The AI will give consistent answers for data extraction but varied suggestions for content generation." |
| **Embeddings**      | Explaining search and RAG. "We'll make your documents searchable by meaning, not just keywords."                               |
| **Hallucinations**  | Managing risk. "Here's our verification workflow to ensure AI outputs are accurate before they reach end users."               |

If you can explain these concepts to a non-technical stakeholder, you're already ahead of 90% of developers working with AI.

## Exercises

Head to the [exercises/](exercises/) directory:

| #   | Exercise                                                                   | Description                                                                         | Est. Time |
| --- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------- |
| 01  | [Token Counting](exercises/starter/01_token_counting.py)                   | Use `tiktoken` to explore how different types of text tokenize — and why it matters | 20 min    |
| 02  | [Temperature Exploration](exercises/starter/02_temperature_exploration.py) | Run the same prompt at different temperatures and document the behavior changes     | 30 min    |
| 03  | [Hallucination Patterns](exercises/starter/03_hallucination_patterns.py)   | Deliberately trigger hallucinations and document the patterns                       | 30 min    |

## Take It Further

- **Read:** [What Are Embeddings?](https://vickiboykis.com/what_are_embeddings/) by Vicki Boykis — the best plain-language explanation of embeddings on the internet
- **Watch:** [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) by Andrej Karpathy — 1 hour that will change how you think about LLMs
- **Explore:** [OpenAI Tokenizer](https://platform.openai.com/tokenizer) — paste text and see how it tokenizes in real time
- **Next module:** [Prompt Engineering](../02-prompt-engineering/) — now that you know how the engine works, learn how to drive
