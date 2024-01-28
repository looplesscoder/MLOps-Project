from flask import Flask, request , render_template 
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

studentapp= Flask(__name__)

app= studentapp

@app.route("/")

