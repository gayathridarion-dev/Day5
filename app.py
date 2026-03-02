# app.py
from flask import Flask, render_template, request
from chatbot import get_song_query
from selenium_player import play_song_on_youtube
import threading

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    song = None
    if request.method == "POST":
        user_input = request.form.get("user_input")
        song = get_song_query(user_input)

        # Use a thread so Flask doesn't block while Selenium runs
        threading.Thread(target=play_song_on_youtube, args=(song,)).start()

    return render_template("index.html", song=song)

if __name__ == "__main__":
    app.run(debug=True)