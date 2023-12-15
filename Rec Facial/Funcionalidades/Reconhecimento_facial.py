import cv2
import numpy as np

reconhecimentoFacial = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detectaImg(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rostos = reconhecimentoFacial.detectMultiScale(gray, 1.3, 5)
    
    if rostos is ():
        return img
    
    for (x, y, w, h) in rostos:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    return img

cap = cv2.VideoCapture(0)

cap.open("http://192.168.0.65:8080/video")

while True:
    check, frame = cap.read()
    frame = detectaImg(frame)
    cv2.imshow("img", frame)
    key = cv2.waitKey(5)
    
    if key == 27:  # Tecla ESC
        break

cap.release()
cv2.destroyAllWindows()