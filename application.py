from flask import Flask, redirect, render_template, request, url_for

import os, sys
import helpers
from analyzer import Analyzer
from nltk.tokenize import TweetTokenizer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():


    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    print(screen_name)
    if not screen_name:
        return redirect(url_for("index"))
    # get screen_name's tweets
    try:
        print("Trying...")
        tweets = helpers.get_user_timeline(screen_name, count=100)
    except TwythonError:
        print("AAAAAAAAARGHH!!!!")
        return render_template("index")

    twt_tokenizer = TweetTokenizer()
    pos_counter = 0
    neg_counter = 0
    neutral_counter = 0

    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    analyzer = Analyzer(positives, negatives)

    # If username isn't valid tweets will be equal to None
    if tweets:
        for tweet in tweets:
            tokens = twt_tokenizer.tokenize(tweet)
            sentiment_counter = 0
            for token in tokens:
                sentiment_counter += analyzer.analyze(token)
            if sentiment_counter > 0:
                pos_counter += 1
            elif sentiment_counter < 0:
                neg_counter += 1
            else:
                neutral_counter += 1
    else:
        return redirect(url_for("index"))
    #print(pos_counter, neg_counter, neutral_counter)
    """
    """

    # generate chart
    chart = helpers.chart(pos_counter, neg_counter, neutral_counter)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
