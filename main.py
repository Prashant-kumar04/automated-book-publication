
from scraper.chapter_scraper import fetch_chapter
from ai_agents.writer_agent import rewrite_chapter
from ai_agents.reviewer_agent import review_chapter
from rl.reward_system import reward_similarity
from versioning.chroma_store import store_version
import os

if __name__ == "__main__":
    URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1. "
    print("[1] Fetching chapter from web...")
    original_text = fetch_chapter(URL)

    print("[2] Rewriting chapter using AI Writer...")
    spun_text = rewrite_chapter(original_text)
    with open("data/chapter_spun.txt", "w", encoding="utf-8") as f:
        f.write(spun_text)

    print("[3] Reviewing rewritten chapter...")
    review_text = review_chapter(spun_text)
    with open("data/chapter_review.txt", "w", encoding="utf-8") as f:
        f.write(review_text)

    print("[4] Awaiting human edits in GUI: Run `python editor_gui/app.py`")
    input("\nPress ENTER after saving your final version via the web editor...\n")

    if os.path.exists("data/chapter_final.txt"):
        with open("data/chapter_final.txt", "r", encoding="utf-8") as f:
            final_text = f.read()

        print("[5] Calculating RL Reward...")
        score = reward_similarity(spun_text, final_text)
        print(f"RL Reward Score: {score:.2f}")

        print("[6] Storing final version in ChromaDB...")
        store_version("chapter1_final", final_text)
        print("[DONE] Workflow completed successfully.")
    else:
        print("[ERROR] Final version not found. Please edit and save from the GUI.")
        