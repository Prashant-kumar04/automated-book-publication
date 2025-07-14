📖 Automated Book Publication Workflow

An intelligent, modular system for scraping book content, rewriting with AI agents, incorporating human reviews, and managing version control with semantic search and voice-based interaction.

✨ Features

🚀 Web Scraping & Screenshot Capture (Playwright)

🤖 AI Writer Agent (Gemini/OpenAI based spinning)

📑 AI Reviewer Agent (LLM-based quality review)

🔗 Human-in-the-Loop GUI Editor (Flask Web App)

🏛️ ChromaDB Versioning + Semantic Search

🔄 RL-based Reward Flow for agent collaboration

🎤 Voice Agent API (optional)

🎨 Workflow Diagram

graph TD
    A[Input URL] --> B[Playwright Scraper + Screenshot]
    B --> C[Original Chapter Text]
    C --> D[AI Writer (Gemini/OpenAI)]
    D --> E[Rewritten Draft]
    E --> F[AI Reviewer Agent]
    F --> G[Final Draft Proposal]
    G --> H[Human-in-the-Loop Editor GUI]
    H --> I[ChromaDB + Voice Agent + RL Reward System]

🔎 Detailed Overview

1. Scraping & Screenshots (Playwright)

Uses headless browser automation to grab full content.

Automatically takes screenshots of the page for visual reference.

2. AI Writer Agent

Sends the chapter to Gemini Pro or OpenAI for "spinning"

Generates creative yet faithful reinterpretation.

3. AI Reviewer Agent

Validates grammar, tone, logical consistency.

Suggests improvements (via prompt-based instruction).

4. Human Editor (Flask GUI)

Launches local web interface for manual finalization.

Allows editing and version locking.

5. RL-Based Reward System

Agents get reward signals for quality, coherence, and acceptance.

Helps shape future writing interactions.

6. ChromaDB + Semantic Search

Stores all versions with embeddings.

Retrieve any version by similarity query.
