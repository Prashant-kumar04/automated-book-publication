from difflib import SequenceMatcher

def reward_similarity(ai_output: str, human_edit: str) -> float:
    return SequenceMatcher(None, ai_output, human_edit).ratio()

if __name__ == "__main__":
    with open("data/chapter_spun.txt", "r") as f:
        ai_output = f.read()
    with open("data/chapter_final.txt", "r") as f:
        human_edit = f.read()
    reward = reward_similarity(ai_output, human_edit)
    print(f"RL Reward Score: {reward:.2f}")