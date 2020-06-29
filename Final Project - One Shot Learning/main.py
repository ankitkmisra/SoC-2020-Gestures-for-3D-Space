print('Preparing program...')

import cv2
import numpy as np
import matplotlib.pyplot as pyplot
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from gestures_utils import *

model = prepare_model()
database = prepare_database(model)

num_to_gesture = {
	'1': 'Fist',
	'2': 'One',
	'3': 'Three',
	'4': 'Two',
	'5': 'Four',
	'6': 'Five',
	'7': 'Yo',
	'8': 'Call me',
	'9': 'Spock',
	'10': 'Gun',
	'11': 'Two-Handed Cross',
	'12': 'A-Okay',
	'13': 'Come Here',
	'14': 'Crocodile',
	'15': 'Kamehameha'
}

print('Ready to go!')

cap = cv2.VideoCapture(0)
img = None

while(True):

	ret, frame = cap.read()

	frame = cv2.rectangle(frame, (350, 150), (550, 350), (255, 0, 0), 1)
	h, w, c = frame.shape
	img = frame[152:348, 352:548, :]
	frame2 = np.zeros((h, w, 3), np.uint8)
	frame2[152:348, 352:548, :] = img
	img = cv2.flip(img, 1)

	min_dist, identity = finder(img, database, model)
	if min_dist < 1.25:
		frame2 = cv2.putText(frame2, num_to_gesture[identity], (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

	cv2.imshow('Frame 1', frame)
	cv2.imshow('Frame 2', frame2)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()