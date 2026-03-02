# chatbot.py

from song_logic import detect_mood, get_song_for_mood

def get_song_query(user_input):
    mood = detect_mood(user_input)
    return get_song_for_mood(mood)