# Project: Steganography with Python

**Group Project by:**

- Ajay Dhungel
- Dhananjaya Kafle
- Suvash Bhandari
- Ram Pukar Singh

Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video. This Flask application allows you to encode messages into images using steganography and decode hidden messages from images.

---

## Features 🚀
- **Encode Message:** Encode a message into an image using steganography.
- **Decode Message:** Decode a hidden message from an encoded image.

---

## Setup 🛠️

### Commands to Clone the repository:
```bash
git clone https://github.com/bsubash2054/image_steganography.git
cd image_steganography
pip install -r requirements.txt
flask run
````

## File Structure 📁

- **.github/**
  - Contains GitHub Actions workflow files for automating tasks like Docker image builds and pushes.
  
- **.idea/**
  - Contains project settings and configurations for JetBrains IDEs (such as PyCharm).
  
- **__pycache__/**
  - Automatically created by Python to store compiled bytecode versions of source files for faster execution.
  
- **static/**
  - Contains static files (like images, CSS, JavaScript) for the Flask application.
  
- **templates/**
  - Contains HTML templates for the Flask application's user interface.
  
- **venv/**
  - Contains the Python virtual environment directory, where dependencies are isolated for the project.
  
- **.gitignore**
  - Specifies files and directories that should be ignored by Git (e.g., local development files, virtual environments).
  
- **Dockerfile**
  - Contains instructions for building a Docker image of the Flask application, specifying its environment and dependencies.
  
- **README.md**
  - The markdown file you are currently editing, providing information about the project, setup, usage, and more.
  
- **app.py**
  - The main Flask application file with routes for encoding and decoding messages using steganography.
  
- **readme.txt**
  - A text file that may contain additional information or instructions related to the project.
  
- **requirements.txt**
  - A file listing all Python dependencies required for the project to run, used for installation via pip.
  
- **steganography.py**
  - A module containing functions for steganography encoding and decoding, used by the Flask application.

---

## Docker Build and Push (GitHub Actions Workflow) 🐳

This project includes a GitHub Actions workflow to automatically build and push the Docker image to Amazon ECR on every push to the main branch.

### Docker Build and Push

- **Trigger:** Automatically runs on every push to the main branch.

#### Steps
1. **Checkout code:** Retrieves the code from the repository.
2. **Configure AWS credentials:** Configures AWS credentials for pushing to Amazon ECR.
3. **Login to Amazon ECR:** Logs in to the Amazon ECR registry.
4. **Get Git Commit ID:** Retrieves the Git commit ID for tagging the Docker image.
5. **Build, Tag, and Push the Image to Amazon ECR:**
   - Builds the Docker image.
   - Tags the image with the Git commit ID.
   - Pushes the image to Amazon ECR.
## Project URL

![image](https://github.com/bsubash2054/image_steganography/assets/162769546/f08da8e4-29eb-472e-9046-a424c6e432ab)

http://a02d3cf2432ea409cb955949bfaca586-50435301.us-east-1.elb.amazonaws.com 
