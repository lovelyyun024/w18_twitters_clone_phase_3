from flask import Flask, render_template
from .config import Config
# !!START SILENT
from .tweets import tweets
import random
# !!END
from .form.form import TweetForm


app = Flask(__name__)

app.config.from_object(Config)

# !!START
@app.route("/")
def index():
    """
    Landing page, displays a random tweet
    """
    tweet = random.choice(tweets)
    return render_template("index.html", tweet=tweet)


@app.route("/feed")
def feed():
    """
    Displays the feed page showing all tweets
    """
    return render_template('feed.html', tweets=tweets)
# !!END


@app.route("/new", method = ["GET", "POST"])
def new():
    form = TweetForm()
    return render_template('new_tweet.html', form=form)

    
