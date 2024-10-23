import os

from flask import Flask, render_template, request

app = Flask(__name__)

IMAGE_DIR = 'static/uploaded_images'
os.makedirs(IMAGE_DIR, exist_ok=True)

import routes


if __name__ == '__main__':
    app.run()
