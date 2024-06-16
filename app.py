#import matplotlib.pyplot as plt
#import pandas as pd
#import numpy as np

from flask import Flask , render_template


app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html',text = "Hello World")

if __name__ == '__main__':
  app.run(debug=True)



