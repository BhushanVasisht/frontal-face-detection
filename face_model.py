import cv2

def detect_faces(blur_frame, frame):
    faces = face_cascade.detectMultiScale(blur_frame, scaleFactor=1.2, minNeighbors=5)

    print(faces)

    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,250), 3)
    return frame
