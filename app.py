from flask import Flask, render_template, request
import steganography

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/encode-message", methods=['POST','GET'])
def encode_message():
    try:
        if request.method == 'POST':
            image = request.files.get('image')
            message = request.values.get("message")
            return steganography.encode(image, message)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500    

    
@app.route("/decode-message", methods=['POST','GET'])
def decode_message():
    if request.method == 'POST':
        image = request.files.get('image')
        return steganography.decode(image)



