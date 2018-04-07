import cv2

def detect_faces(blur_frame, frame):
    faces = face_cascade.detectMultiScale(blur_frame, scaleFactor=1.2, minNeighbors=5)

    print(faces)

    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 3)
    return frame

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("D:/UDEMY/Python Mega Course - 11 Projects/18 Python for Image and Video Processing with OpenCV/170 Files/haarcascade_frontalface_default.xml")

while True:
    ret,frame = cap.read()
    gray_frame  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur_frame = cv2.GaussianBlur(gray_frame, (5,5), 3)
    cv2.imshow("Detect Frontal Faces Only",  detect_faces(blur_frame,frame))
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
