from flask import Flask, request, render_template , jsonify
import pandas as pd
from keras.models import load_model

# Load the saved model
model = load_model('my_model.h5')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('multiple_inputs.html')  # Render the form template

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the form data
        feature1 = float(request.form['age'])
        feature2 = float(request.form['sex'])
        feature3 = float(request.form['cp'])
        feature4 = float(request.form['trtbps'])
        feature5 = float(request.form['chol'])
        feature6 = float(request.form['fbs'])
        feature7 = float(request.form['restecg'])
        feature8 = float(request.form['thalachh'])
        feature9 = float(request.form['exng'])
        feature10 = float(request.form['oldpeak'])
        feature11 = float(request.form['slp'])
        feature12 = float(request.form['caa'])
        feature13 = float(request.form['thall'])

        # Create a DataFrame from features
        user_data = pd.DataFrame({'feature1': [feature1], 'feature2': [feature2], 'feature3': [feature3], 'feature4': [feature4], 'feature5': [feature5], 'feature6': [feature6], 'feature7': [feature7], 'feature8': [feature8], 'feature9': [feature9], 'feature10': [feature10], 'feature11': [feature11], 'feature12': [feature12], 'feature13': [feature13]})

        # Preprocess data if necessary (replace with your preprocessing logic)
        # ... your preprocessing steps ...

        # Convert DataFrame to NumPy array
        user_data_array = user_data.to_numpy()

        # Make predictions
        predictions = model.predict(user_data_array)
        prediction = predictions[0].item()
        rounded_prediction = round(prediction)
        
        if rounded_prediction == 0:
            rounded_prediction = "You are not risk"
        else:
            rounded_prediction = "You are risk!!"
        

        # Process predictions (replace with your logic based on model output)
        processed_predictions = rounded_prediction  

        #return render_template('response.html', prediction=processed_predictions)  # Render response template with prediction
        return jsonify({'prediction': processed_predictions}) #return with jsontify

    except Exception as e:
        return render_template('error.html', error=str(e)), 400  # Handle errors and return appropriate status code

if __name__ == '__main__':
    app.run(debug=True)
