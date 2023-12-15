import cv2

webcam = cv2.VideoCapture()
ip = "http://192.168.0.65:8080/video"
webcam.open(ip)

while True:
    check, img = webcam.read()
    cv2.imshow("img", img)
    key = cv2.waitKey(5)
    if key == 27 : #ESC Key
        break


