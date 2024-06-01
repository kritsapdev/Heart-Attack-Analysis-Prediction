from flask import Flask , render_template
import torch
from transformers import pipeline

app = Flask(__name__)

pipe = pipeline("text-generation", model="WizardLM/WizardMath-7B-V1.0")
print(pipe("The goal in life is"))


@app.route('/')
def index():
  script_value = pipe("The goal in life is")
  return render_template('index.html', script_value=script_value)

if __name__ == '__main__':
  app.run(debug=True)



