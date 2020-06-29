import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('me_color.avi', fourcc, 20.0, (640, 480))
out2 = cv2.VideoWriter('me_grayscale.avi', fourcc, 20.0, (640, 480))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
	ret, frame = cap.read()
	if ret:
		out1.write(frame)
		grayvid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		grayvid = cv2.cvtColor(grayvid, cv2.COLOR_GRAY2BGR)
		out2.write(grayvid)
		cv2.imshow('frame', frame)
		cv2.imshow('grayframe', grayvid)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
out1.release()
out2.release()
cv2.destroyAllWindows()