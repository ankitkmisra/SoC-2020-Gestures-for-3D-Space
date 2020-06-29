from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import pickle
import sqlite3
import os
import numpy as np

app = Flask(__name__)

cur_dir = os.path.dirname(__file__)
model = pickle.load(open(os.path.join(cur_dir, 'random_forest_housing.pkl'), 'rb'))
db = os.path.join(cur_dir, 'reviews.sqlite')

def predict(document):
	
