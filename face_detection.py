import cv2
import numpy as np

inp_img = cv2.imread("D:/UDEMY/Python Mega Course - 11 Projects/18 Python for Image and Video Processing with OpenCV/170 Files/news.jpg",1)

gray_img = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier("D:/UDEMY/Python Mega Course - 11 Projects/18 Python for Image and Video Processing with OpenCV/170 Files/haarcascade_frontalface_default.xml")

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5)

print(faces)

for x,y,w,h in faces:
    cv2.rectangle(inp_img, (x,y), (x+w, y+h), (0,255,0), 3)

cv2.imshow("Detect faces", inp_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
