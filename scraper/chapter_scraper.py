from playwright.sync_api import sync_playwright
import os
import re

def fetch_chapter(url: str, save_dir: str = "data"):
    os.makedirs(save_dir, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        # Wait for main content
        page.wait_for_selector("#mw-content-text")

        # Get text content
        content = page.inner_text("#mw-content-text")
        cleaned_text = re.sub(r"\s+", " ", content.strip())

        # Save raw and cleaned content
        with open(f"{save_dir}/chapter_raw.txt", "w", encoding="utf-8") as f:
            f.write(content)
        with open(f"{save_dir}/chapter_clean.txt", "w", encoding="utf-8") as f:
            f.write(cleaned_text)

        # Screenshot
        page.screenshot(path=f"{save_dir}/chapter_screenshot.png", full_page=True)
        browser.close()

        return cleaned_text

if __name__ == "__main__":
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    fetch_chapter(url)
