# ai_model.py

from song_logic import detect_mood

def analyze_mood(user_input):
    """Wrapper for chatbot or other modules"""
    return detect_mood(user_input)