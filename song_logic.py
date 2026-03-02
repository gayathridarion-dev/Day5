# song_logic.py

def detect_mood(user_input):
    """Simple mood detection"""
    user_input = user_input.lower()
    if any(word in user_input for word in ["happy", "joy", "excited"]):
        return "happy"
    elif any(word in user_input for word in ["sad", "down", "unhappy"]):
        return "sad"
    return "neutral"


def get_song_for_mood(mood):
    """Return a song based on mood"""
    if mood == "happy":
        return "Happy - Pharrell Williams"
    elif mood == "sad":
        return "Someone Like You - Adele"
    return "Shape of You - Ed Sheeran"