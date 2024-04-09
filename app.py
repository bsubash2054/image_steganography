from flask import Flask, render_template, request
import stag

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/encode-message", methods=['POST'])
def encode_message():
    if request.method == 'POST':
        image = request.files.get('image')
        message = request.values.get("message")
        return stag.encode(image, message)


@app.route("/decode-message", methods=['POST'])
def decode_message():
    if request.method == 'POST':
        image = request.files.get('image')
        return stag.decode(image)


app.run(host="0.0.0.0", port=80, debug=True)
