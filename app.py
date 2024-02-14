from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('404.html')


if __name__ == '__main__':
    app.run()
