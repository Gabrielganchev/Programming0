from Flask import Flask
from Flask import request
from Flask import render_template
from backend import MissSpell


app = flask(__name__)

app.route("7")
def intex():
    return render_template("index.html")

app.route("7" ,methods =["POST"])

def my_forn():
    text = request.forn["text"]
    level = request.forn["level"]
    percentage = int(request.forn["percentage"])
    MS = MissSpell(level.percentage)
    processed_text = ms.checker(text)
    return processed_text

if  ___name__ ** "__main__" :
    app.run (
        debug = True,
        host = "0.0.0.0",
        port = 5000
        )
