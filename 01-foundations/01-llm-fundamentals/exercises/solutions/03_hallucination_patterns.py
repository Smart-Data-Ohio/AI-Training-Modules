"""
Exercise 03: Hallucination Patterns — Solution
================================================
Example results and completed verification checklist.
Your specific results will vary by model and date.
"""

# NOTE: These are representative results. The specific hallucinations
# you encounter will depend on the model, version, and date.

results = {
    "fake_paper": {
        "model_used": "Claude 3.5 Sonnet",
        "did_hallucinate": True,
        "what_it_said": "Provided 3 papers with plausible-sounding authors, journal names, and DOIs. Two of the three papers don't exist.",
        "how_you_verified": "Searched DOIs on doi.org, searched paper titles on Google Scholar.",
        "notes": "The model was very confident. The fabricated DOIs followed the correct format (10.xxxx/...) which makes them look real at first glance.",
    },
    "fake_url": {
        "model_used": "Claude 3.5 Sonnet",
        "did_hallucinate": True,
        "what_it_said": "Generated a plausible URL like docs.smartdataohio.com/developers or similar.",
        "how_you_verified": "Tried to visit the URL — it doesn't exist.",
        "notes": "Some models will admit they don't know the URL. Others fabricate one that looks legitimate.",
    },
    "wrong_facts": {
        "model_used": "Claude 3.5 Sonnet",
        "did_hallucinate": True,
        "what_it_said": "Gave a specific number (e.g., 6,514 windows) with apparent confidence.",
        "how_you_verified": "Cross-referenced multiple sources. The exact number varies by source, suggesting even 'real' answers are uncertain.",
        "notes": "This is a tricky one — the model gives a specific number confidently, but the real answer isn't well-documented. Shows how models fabricate precision.",
    },
    "fake_api": {
        "model_used": "Claude 3.5 Sonnet",
        "did_hallucinate": False,
        "what_it_said": "Correctly identified that QuantumForestClassifier doesn't exist in sklearn. Suggested real alternatives.",
        "how_you_verified": "Checked sklearn docs.",
        "notes": "Models are getting better at catching non-existent APIs, but this varies. Older and smaller models are much more likely to hallucinate fake APIs.",
    },
    "fake_person": {
        "model_used": "Claude 3.5 Sonnet",
        "did_hallucinate": True,
        "what_it_said": "Generated a detailed biography of a fictional 'Dr. Sarah Chen' with specific research details, publication history, and MIT affiliations.",
        "how_you_verified": "Searched MIT faculty directory, Google Scholar, LinkedIn.",
        "notes": "The fictional composite is one of the most dangerous patterns. The model blends real details (MIT, transformer models, protein folding) into a convincing but fake narrative.",
    },
    "recent_events": {
        "model_used": "Claude 3.5 Sonnet",
        "did_hallucinate": True,
        "what_it_said": "Either admitted uncertainty about future events or generated plausible-sounding announcements based on past events.",
        "how_you_verified": "Checked against actual event coverage.",
        "notes": "Models with knowledge cutoffs will either admit they don't know or extrapolate from past events. Both are unreliable for recent/future information.",
    },
}

PATTERN_ANALYSIS = """
Hallucination Pattern Analysis
===============================

Pattern                  | Hallucinated? | Confidence Level | Danger Level
-------------------------|---------------|-----------------|-------------
Fabricated citations     | YES           | Very High        | CRITICAL — looks completely real
Fabricated URLs          | YES           | High             | HIGH — users will click and get 404s
Wrong specific facts     | YES           | High             | MEDIUM — often impossible to verify quickly
Fake APIs/libraries      | Sometimes     | Medium           | HIGH — broken code wastes developer time
Fictional composites     | YES           | Very High        | CRITICAL — most convincing hallucination type
Recent events            | YES           | Medium           | HIGH — no way to verify without external sources

Key observations:
- Fabricated citations and fictional composites are the most dangerous because
  they're the most convincing. The model generates plausible authors, journals,
  and DOIs that follow real formatting patterns.
- The model rarely says "I don't know" unless specifically trained to.
- Confidence level does NOT correlate with accuracy. The model sounds just as
  confident when hallucinating as when it's correct.
"""

print(PATTERN_ANALYSIS)

VERIFICATION_CHECKLIST = """
AI Output Verification Checklist
=================================
Before including AI-generated content in any client-facing deliverable:

[x] 1. Verify all citations, URLs, and references independently
      (Google Scholar, DOI lookup, direct URL check)
[x] 2. Cross-reference specific facts (dates, numbers, statistics)
      against primary sources
[x] 3. Check that any mentioned people, organizations, or products
      actually exist
[x] 4. Test any generated code — don't just read it, run it
[x] 5. If the output sounds surprisingly specific or detailed about
      something obscure, treat it as suspicious until verified

Red flags to watch for:
- Suspiciously specific numbers for things that aren't well-documented
- DOIs, URLs, or ISBNs (models love fabricating these in correct formats)
- Named individuals with detailed bios you can't find online
- API functions or library features that don't appear in official docs
- Recent event details that are beyond the model's knowledge cutoff
"""

print(VERIFICATION_CHECKLIST)
