import cv2  # Importing the OpenCV library for computer vision tasks

# Loading the Haar Cascade classifier for detecting faces
face_cap = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Initializing the video capture object to use the default camera (0)
video_cap = cv2.VideoCapture(0)

# Starting an infinite loop to continuously read frames from the webcam
while True:
    # Capturing each frame from the video capture object
    ret, video_data = video_cap.read()
    
    # Displaying the captured frame in a window named 'frame'
    cv2.imshow('frame', video_data)
    
    # Converting the captured frame to grayscale for face detection
    gray = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    
    # Detecting faces in the grayscale image using the Haar Cascade classifier
    faces = face_cap.detectMultiScale(gray, 1.1, 5, cv2.CASCADE_SCALE_IMAGE)
    
    # Looping through the detected faces and drawing rectangles around them in the original frame
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Drawing rectangle with green color
    
    # Displaying the video stream with rectangles around detected faces in a window named 'video_live'
    cv2.imshow('video_live', video_data)

    # Printing the current frame data to the console (for debugging purposes)
    print(video_data)

    # Checking if the 'q' key is pressed to break the loop and exit
    if cv2.waitKey(10) == ord('q'):
        break

# Releasing the video capture object to free up resources after exiting the loop
video_cap.release()

# Destroying all OpenCV windows opened by the program
cv2.destroyAllWindows()
