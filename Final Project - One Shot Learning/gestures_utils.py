import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import os, shutil
import tensorflow as tf
from keras.models import model_from_json
import keras.backend as K

def prepare_model():
	"""
	Loads model architecture from JSON file and model weights from H5 file.
	"""
	json_file = open('final_gestures_model.json', 'r')
	model_json = json_file.read()
	json_file.close()
	model = model_from_json(model_json)
	model.load_weights('final_gestures_weights.h5')

	return model

def img_to_encoding(image, model):
	"""
	Returns the encoding for a given image.

	Parameters:
	image_path - Path to the image to be encoded.
	model - The model used for classification.
	"""
	image = cv2.resize(image, (96,96))
	img = image/255.
	encoding = model.predict_on_batch(np.array([img]))

	return encoding

def finder(image, database, model):
	"""
	Returns the gesture class closest to the given image (and the corresponding distance), using L2 norm of difference between encodings to measure distance.

	Parameters:
	image_path - Path to the image to be classified.
	database - A dictionary containing the encodings of sample images from all gesture classes.
	model - The model used for classification.
	"""
	encoding = img_to_encoding(image, model)

	min_dist = 100

	for (name, db_enc) in database.items():
	    dist = np.linalg.norm(db_enc - encoding)
	    if dist < min_dist:
	        min_dist = dist
	        identity = name

	return min_dist, identity

def prepare_database(model):
	"""
	Loads database of hand gestures for one-shot recognition.
	"""
	database = {}
	for gesture in os.listdir('gestures_dataset_2'):
		image1 = os.listdir(os.path.join('gestures_dataset_2', gesture))[3]
		img = cv2.imread(os.path.join('gestures_dataset_2', gesture, image1))
		database[gesture] = img_to_encoding(img, model)

	return database