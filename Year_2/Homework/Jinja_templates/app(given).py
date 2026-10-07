from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome in to our album site"

@app.route("/album")
def album():
    album = {
        "title": "Travelling Without Moving",
        "artist": "Jamiroquai",
        "year": "1996",
        "genre": "Funk"
    }

    return render_template("album.html", album = album)

if __name__ == "__main__":
    app.run(debug=True)
