# Deepfake Detection Application

This is a Flask-based web application for detecting deepfake images. The application utilizes a trained Keras model to classify uploaded images as either "Real" or "Fake."

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Features

- Upload an image to determine if it is real or a deepfake.
- User-friendly web interface.
- Powered by a deep learning model for high accuracy.

## Technologies Used

- Flask: A lightweight WSGI web application framework for Python.
- Keras: A deep learning API running on top of TensorFlow.
- NumPy: A library for numerical computing in Python.
- PIL (Pillow): A Python Imaging Library for image processing.
- HTML/CSS: For front-end development.

## Getting Started

### Prerequisites

- Python 3.6 or newer
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/deepfake-detection.git
   cd deepfake-detection
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Download or prepare a Keras model:**
   Ensure you have a trained Keras model (e.g., modelo_detector_caras.keras) in the project directory.

### Usage
1. **Run the Flask application:**
```bash
python app.py
```
2. **Navigate to the web interface:**
   Open your web browser and go to http://127.0.0.1:5000/.
   
3. **Upload an image:**
   Use the upload button to select an image file and click "Upload" to see the prediction results.

### Model Training
To train your own deepfake detection model, use the Keras library and follow these general steps:

- Load and preprocess your dataset.
- Define your model architecture using Sequential or functional API.
- Compile the model with appropriate loss function and optimizer.
- Train the model on your data.
- Save the trained model to a .keras file.

### Contributing
Contributions are welcome! If you would like to contribute to this project, please fork the repository and create a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

