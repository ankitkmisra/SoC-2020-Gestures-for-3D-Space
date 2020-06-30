import cv2
import os

os.mkdir('gestures_data_2/')

num_classes = 15
pics_per_class = 25

for i in range(1, num_classes+1):
   os.mkdir(f'gestures_data_2/{i}/')

count = 0
cap = cv2.VideoCapture(0)

while(True):
    
    ret, frame = cap.read()

    frame = cv2.rectangle(frame, (150, 150), (350, 350), (255, 0, 0), 0)
    frame2 = frame[152:348, 152:348, :]
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(f'gestures_data_2/{int(count/pics_per_class)+1}/{count%pics_per_class+1}.jpg', frame2)
        print(int(count/pics_per_class)+1, count%pics_per_class+1)
        count += 1

    if count == num_classes * pics_per_class:
        break

cap.release()
cv2.destroyAllWindows()