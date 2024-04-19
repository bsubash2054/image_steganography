from flask import Flask, render_template, request
import steganography

app = Flask(__name__)


# Route for displaying encode and decode message forms. This is the default route of the site.
@app.route("/")
def home():
    return render_template("index.html")


# Route for encoding message in image. Only accepts POST requests.
@app.route("/encode-message", methods=['POST'])
def encode_message():
    """
    This function handles encoding message inside the image.
    :return: The path of the encoded image that the users can download.
    """
    if request.method == 'POST':
        image = request.files.get('image')
        message = request.values.get("message")
        return steganography.encode(image, message)


# Route for decoding messages. Only accepts POST requests
@app.route("/decode-message", methods=['POST'])
def decode_message():
    """
    This function handles the decoding of message from the image.
    :return: The text that is decoded. This text contains <message> + <timestamp>. These two items are
    separated by the frontend and displayed accordingly.
    """
    if request.method == 'POST':
        image = request.files.get('image')
        return steganography.decode(image)


app.run(host="0.0.0.0", port=8000, debug=True)
