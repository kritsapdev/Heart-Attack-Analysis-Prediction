<h1>Title: Heart Attack Analysis & Prediction App</center></h1>

<h2>Description:</h2>

This project presents a web application that employs deep learning to predict the likelihood of heart attacks based on patient data. It's built using the following technologies:

<li>Backend: Flask (Python web framework) for run prediction model my_model.h5 to serve predictions.</li>
<li>Deep Learning: Keras (TensorFlow library) for building and training a prediction model using heart attack data from Kaggle.</li>
<li>Frontend: Bootstrap (CSS framework) for a user-friendly and responsive interface.</li>
<li>Model Storage: The trained model is saved as my_model.h5 for use within the Flask app.</li>

<h2>Features:</h2>

Predicts the risk of heart attacks based on input data.
Provides a user-friendly interface for data entry and prediction visualization.
Leverages a trained Keras model for accurate predictions.
Ready for deployment (AWS deployment details to be added in a this document later).
<h2>Installation:</h2>

Prerequisites: Ensure you have Python (3.x) and pip installed.
Virtual Environment (Recommended): Create a virtual environment using python -m venv .venv and activate it: source .venv/bin/activate (Windows: .venv\Scripts\activate).
Install Dependencies: Run pip install -r requirements.txt.
Usage:
Activate Environment : source .venv/bin/activate (Windows: .venv\Scripts\activate).
Run the App: Navigate to the project directory and start the Flask development server: python app.py.
Access the App: Open http://localhost:5000/ in your web browser.
Provide Patient Data: Enter relevant patient information through the provided interface.
Get Predictions: Click the "Send" button to receive the predicted risk of a heart attack.
Deployment (AWS):

(Detailed instructions will be provided in this document later.)
