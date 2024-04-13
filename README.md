Project: Steganography with Flask
Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video. This Flask application allows you to encode messages into images using steganography and decode hidden messages from images.

Features 🚀
Encode Message: Encode a message into an image using steganography.
Decode Message: Decode a hidden message from an encoded image.
Setup 🛠️
Clone the repository:

bash
Copy code
git clone https://github.com/bsubash2054/image_steganography.git
cd image_steganography
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Run the Flask application:

bash
Copy code
flask run
The app will be running at http://localhost:8000.

Usage 📝
Encode Message:

Navigate to http://localhost:8000/ in your browser.
Choose an image file and enter the message you want to encode.
Click the "Encode" button.
The encoded image will be downloaded automatically.
Decode Message:

Navigate to http://localhost:8000/ in your browser.
Choose the encoded image.
Click the "Decode" button.
The hidden message will be displayed.
File Structure 📁
app.py: Flask application with routes for encoding and decoding.
steganography.py: Module containing functions for steganography encoding and decoding.
Dockerfile: Docker configuration for building the Flask app.
requirements.txt: List of Python dependencies.
Docker Build and Push (GitHub Actions Workflow) 🐳
This project includes a GitHub Actions workflow to automatically build and push the Docker image to Amazon ECR on every push to the main branch.

Docker Build and Push
Trigger: Automatically runs on every push to the main branch.
Steps
Checkout code: Retrieves the code from the repository.
Configure AWS credentials: Configures AWS credentials for pushing to Amazon ECR.
Login to Amazon ECR: Logs in to the Amazon ECR registry.
Get Git Commit ID: Retrieves the Git commit ID for tagging the Docker image.
Build, Tag, and Push the Image to Amazon ECR:
Builds the Docker image.
Tags the image with the Git commit ID.
Pushes the image to Amazon ECR.
