import os
from flask import Flask, render_template, request
import giphypop
app = Flask(__name__)

g = giphypop.Giphy()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/results")
def results():
    term = request.values.get('term')
    results = g.search(term)
    return render_template('results.html', results=results, term=term)

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
