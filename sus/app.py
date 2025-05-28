from flask import Flask, render_template

import os

app = Flask(__name__)
app.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/report', methods=['GET'])
def report():
    return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)