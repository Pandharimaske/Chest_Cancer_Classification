from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.cnnClassifier.utils.common import decodeImage
from src.cnnClassifier.pipeline.prediction_pipeline import PredictionPipeline

# Environment setup
os.putenv("LANG", 'en_US.UTF-8')
os.putenv("LC_ALL", 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

# Client Application class
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

# Route: Home
@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template('index.html')

# Route: Train
@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully"

# Route: Predict
@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)
        result = clApp.classifier.predict()  # Corrected the typo here
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Initialize client app instance
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080)  # For AWS deployment