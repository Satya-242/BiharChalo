from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

# Folder paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.abspath(os.path.join(BASE_DIR, '..', 'Generate test csv'))
IMAGE_FOLDER = os.path.join(BASE_DIR, 'image')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(IMAGE_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle file upload
        if 'csvfile' not in request.files:
            return "No file part", 400
        file = request.files['csvfile']
        if file.filename == '':
            return "No selected file", 400
        if file and file.filename.endswith('.csv'):
            save_path = os.path.join(UPLOAD_FOLDER, 'sampled_transactions.csv')
            file.save(save_path)
            return redirect(url_for('report'))
        else:
            return "Invalid file type. Please upload a CSV.", 400
    return render_template('index.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/image/<filename>')
def image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

@app.route('/csv/<filename>')
def csvfile(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)