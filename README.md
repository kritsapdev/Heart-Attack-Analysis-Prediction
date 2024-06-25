<h1>Title: Heart Attack Analysis & Prediction App</center></h1>

<h2>Description:</h2>

This project presents a web application that employs deep learning to predict the likelihood of heart attacks based on patient data. It's built using the following technologies:

<li>Backend: Flask (Python web framework) for run prediction model my_model.h5 to serve predictions.</li>
<li>Deep Learning: Keras (TensorFlow library) for building and training a prediction model using heart attack data from Kaggle.</li>
<li>Frontend: Bootstrap (CSS framework) for a user-friendly and responsive interface.</li>
<li>Model Storage: The trained model is saved as my_model.h5 for use within the Flask app.</li>

<h2>Features:</h2>

<li>Predicts the risk of heart attacks based on input data.</li>
<li>Provides a user-friendly interface for data entry and prediction visualization.</li>
<li>Leverages a trained Keras model for accurate predictions.</li>
<li>Ready for deployment (AWS deployment details to be added in a this document later).</li>
<h2>Installation:</h2>

<li>Prerequisites: Ensure you have Python (3.x) and pip installed.</li>
<li>Virtual Environment (Recommended): Create a virtual environment using python -m venv .venv and activate it: source .venv/bin/activate (Windows: .venv\Scripts\activate).</li>
<li>Install Dependencies: Run pip install -r requirements.txt.</li>
<h2>Usage:</h2>
<li>Activate Environment : source .venv/bin/activate (Windows: .venv\Scripts\activate).</li>
<li>Run the App: Navigate to the project directory and start the Flask development server: python app.py.</li>
<li>Access the App: Open http://localhost:5000/ in your web browser.</li>
<li>Provide Patient Data: Enter relevant patient information through the provided interface.</li>
<li>Get Predictions: Click the "Send" button to receive the predicted risk of a heart attack.</li>

<h2>Deployment (AWS):</h2>

(Detailed instructions will be provided in this document later.)
