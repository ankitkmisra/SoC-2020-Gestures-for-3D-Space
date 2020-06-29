import cv2

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
	ret, frame = cap.read()
	if ret:
		grayvid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame', grayvid)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
cv2.destroyAllWindows()