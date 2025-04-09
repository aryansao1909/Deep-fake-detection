from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import io
from PIL import Image

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
model = load_model('modelo_detector_caras.keras')

# Define the expected image size (for EfficientNetB0)
IMG_SIZE = (128, 128)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    # Preprocess the image
    try:
        img = Image.open(io.BytesIO(file.read()))
        img = img.resize(IMG_SIZE)  # Resize the image to (128, 128)
        img_array = img_to_array(img) / 255.0  # Normalize the image
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    # Check the shape of the input for debugging
    print("Input shape after preprocessing:", img_array.shape)  # Should print (1, 128, 128, 3)

    # No need to reshape; keep the shape (1, 128, 128, 3) for the model
    # Make a prediction
    try:
        prediction = model.predict(img_array)
        class_label = (prediction > 0.5).astype(int)[0][0]
        
        # Map class labels to meaningful results
        if class_label == 1:
            result = "Real"  # Class 1 indicates Real
        elif class_label == 0:
            result = "Fake"  # Class 0 indicates Fake
        else:
            result = "Unknown"  # Fallback for unexpected cases
        
        return jsonify({'result': result, 'class': int(class_label)}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
 