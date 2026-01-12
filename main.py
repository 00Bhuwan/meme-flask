from flask import Flask, render_template
from meme.meme_flask import get_meme

app = Flask(__name__)

@app.route('/')
def index():
    meme_pic, subreddit = get_meme()
    if meme_pic is None:
        return "api is down"
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == '__main__':
    app.run(debug=True)
