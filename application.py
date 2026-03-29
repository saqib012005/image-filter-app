from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import cv2
from filters import apply_filter

application = Flask(__name__)   # ✅ FIXED

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
application.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER


@application.route('/')
def home():
    return render_template('index.html')


@application.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    filter_name = request.form['filter']

    if file:
        filepath = os.path.join(application.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        image = cv2.imread(filepath)
        filtered = apply_filter(image, filter_name)

        output_path = os.path.join(application.config['OUTPUT_FOLDER'], "output.png")
        cv2.imwrite(output_path, filtered)

        return render_template('index.html', output_image="output.png")

    return redirect(url_for('home'))


@application.route('/download')
def download():
    path = os.path.join(application.config['OUTPUT_FOLDER'], "output.png")
    return send_file(path, as_attachment=True)