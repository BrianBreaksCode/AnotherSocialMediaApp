from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    random_number = random.randint(1, 10)
    return render_template('index.html', random_number=random_number)

app.run(host="0.0.0.0", port=8008, debug=True)