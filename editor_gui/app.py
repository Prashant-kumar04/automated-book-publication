from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

# Tries data/chapter_spun.txt first, falls back to editor_gui/draft_output.txt
possible_drafts = [
    os.path.join("data", "chapter_spun.txt"),
    os.path.join("editor_gui", "draft_output.txt")
]

def find_draft():
    for path in possible_drafts:
        if os.path.exists(path):
            return path
    return None

@app.route("/", methods=["GET", "POST"])
def editor():
    draft_file = find_draft()

    if request.method == "POST":
        edited_text = request.form["edited_text"]
        with open(os.path.join("data", "final_version.txt"), "w", encoding="utf-8") as f:
            f.write(edited_text)
        return "✅ Final version saved. You can close this tab and press ENTER in the terminal."

    draft_text = ""
    if draft_file:
        with open(draft_file, "r", encoding="utf-8") as f:
            draft_text = f.read()

    html = """
    <h1>Edit and Finalize the Chapter</h1>
    <form method="POST">
        <textarea name="edited_text" style="width:100%;height:70vh;">{{draft}}</textarea><br>
        <button type="submit">💾 Save Final Version</button>
    </form>
    """
    return render_template_string(html, draft=draft_text)

if __name__ == "__main__":
    app.run(debug=True)
