from flask import Flask, render_template, request
from chatbot import get_song_query
from automation import play_song_on_youtube

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    song = None
    if request.method == "POST":
        user_input = request.form.get("user_input")
        song = get_song_query(user_input)
        play_song_on_youtube(song)  # Opens song in browser automatically
    return render_template("index.html", song=song)

if __name__ == "__main__":
    app.run(debug=True)