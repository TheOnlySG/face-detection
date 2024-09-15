import cv2
face_cap= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)
while True:
    ret, video_data = video_cap.read()
    cv2.imshow('frame',video_data)
    gray = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(gray , 1.1 , 5, cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,x+h),(0,255,0), 3)
    cv2.imshow('vide_live',video_data)
    print(video_data)

    if cv2.waitKey(10) == ord('q'):
        break
video_cap.release()
cv2.destroyAllWindows()