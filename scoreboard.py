import json
import os
from pathlib import Path


LEADERBOARD_FILE = "leaderboard.json"


def load_leaderboard():
    """
    Load leaderboard from JSON file.
    Returns a list of dicts: [{"name": str, "score": int}, ...]
    Sorted by score (ascending). Empty list if file doesn't exist.
    """
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    
    try:
        with open(LEADERBOARD_FILE, "r") as f:
            data = json.load(f)
            # Ensure it's a list and sorted
            if not isinstance(data, list):
                return []
            return sorted(data, key=lambda x: x.get("score", float("inf")))
    except (json.JSONDecodeError, IOError):
        return []


def save_leaderboard(leaderboard):
    """
    Save leaderboard to JSON file.
    leaderboard: list of dicts [{"name": str, "score": int}, ...]
    """
    try:
        with open(LEADERBOARD_FILE, "w") as f:
            json.dump(leaderboard, f, indent=2)
    except IOError as e:
        print(f"Error saving leaderboard: {e}")


def add_score(name, score):
    """
    Add a score to the leaderboard and return whether it's a new high score.
    Returns: (is_new_high_score: bool, high_score: int)
    """
    leaderboard = load_leaderboard()
    
    # Get current high score (lowest number of guesses)
    current_high_score = None
    if leaderboard:
        current_high_score = leaderboard[0]["score"]
    
    # Check if new score is a high score
    is_new_high = current_high_score is None or score < current_high_score
    
    # Add the new score
    leaderboard.append({"name": name, "score": score})
    leaderboard = sorted(leaderboard, key=lambda x: x["score"])
    
    # Save back to file
    save_leaderboard(leaderboard)
    
    return is_new_high, current_high_score


def get_high_score():
    """
    Get the current high score (lowest number of guesses).
    Returns: int or None if no scores yet.
    """
    leaderboard = load_leaderboard()
    if leaderboard:
        return leaderboard[0]["score"]
    return None


def format_leaderboard(limit=10):
    """
    Format leaderboard for display.
    Returns a formatted string with top scores.
    """
    leaderboard = load_leaderboard()
    
    if not leaderboard:
        return "No scores yet."
    
    lines = ["LEADERBOARD (Fewest Guesses):"]
    lines.append("-" * 50)
    
    for i, entry in enumerate(leaderboard[:limit], 1):
        name = entry.get("name", "Unknown")
        score = entry.get("score", "?")
        lines.append(f"{i:2}. {name:20} {score:3} guesses")
    
    lines.append("-" * 50)
    return "\n".join(lines)


def clear_leaderboard():
    """
    Clear the leaderboard file (for testing/reset).
    """
    if os.path.exists(LEADERBOARD_FILE):
        os.remove(LEADERBOARD_FILE)
