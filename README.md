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

📝 Sequence of Steps
 sequenceDiagram
    participant U as User
    participant P as Playwright
    participant W as AI Writer
    participant R as AI Reviewer
    participant H as Human Editor
    participant DB as ChromaDB

    U->>P: Provide book URL
    P->>P: Scrape and capture screenshot
    P->>W: Send original text
    W->>R: Submit rewritten draft
    R->>H: Reviewed content
    H->>DB: Save final version with feedback


🚀 Setup Instructions
# 1. Clone the repository
$ git clone https://github.com/your-username/automated-book-publication.git
$ cd automated-book-publication

# 2. Create virtual environment
$ python -m venv .venv
$ source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install requirements
$ pip install -r requirements.txt

# 4. Create .env file (do not share this!)
GEMINI_API_KEY=your_gemini_key
OPENAI_API_KEY=your_openai_key

# 5. Run main pipeline
$ python main.py

# 6. When prompted: open GUI to finalize
$ python editor_gui/app.py

💬 Customization Tips

Replace rewrite_chapter logic with your own agent logic.

Switch to ElevenLabs for voice API.

Add GPT reward calibration via RLHF.

Use LangChain instead of native OpenAI/Gemini calls (optional).

🚫 Disclaimer

This project is intended only for educational evaluation. You retain all rights to your code. No commercial usage involved by evaluators.

🌟 Contributors

👤 Prashant Kumar — Developer




