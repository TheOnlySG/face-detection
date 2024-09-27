# Project About :
the face detection program detects your face using harrcascade and puts a square around your face.
the camera named program is a image capturing program .
haarcascade_frontalface_default.xml must bekept in the same folder which contains the facedetection program.

library used = opencv
# how to install opencv?
type the following in your terminal and hit enter. 

pip install opencv-python

it would install open cv and some other essential libraries.
# opencv functions used :
**1)cv2.videocapture()**--
cv2.VideoCapture(0) opens the default camera, and you can pass 1 or other indices for different cameras if available.
cv2.VideoCapture('filename') opens a video file (like .mp4, .avi, etc.).

**2)cam.read()**--
The cam.read() function in OpenCV (where cam is the VideoCapture object) reads a frame from the camera or video file.
frame is passed in this...('file name',frame)

**3)cv2.imshow()**--
The cv2.imshow() function in OpenCV is used to display an image or a frame in a window. It opens a window and shows the image passed to it.

**4)cv2.waitkey()**--
The cv2.waitKey() function is needed after cv2.imshow() because it waits for a key press, allowing the window to stay open. Without it, the window would close immediately.
cv2.waitKey(0) means the window will wait indefinitely for a key press before closing.
cv2.waitKey(ms) means it will wait for a specified number of milliseconds before automatically closing.

**5)cv2.imwrite()**--
The cv2.imwrite() function in OpenCV is used to save an image to a file. It writes the image data (typically a NumPy array) to the specified file path.
cv2.imwrite(filename, image)

**6)cv2.cvtcolor()**--
The cv2.cvtColor() function in OpenCV is used to convert an image from one color space to another. It is particularly useful for converting between different color representations, such as converting an image from BGR (default in OpenCV) to grayscale, RGB, HSV, etc.
cv2.cvtColor(src, code)

**7)detectMultiscale()**--
In OpenCV, the cv2.detectMultiScale() function is typically used for object detection, most commonly with Haar cascades or HOG (Histogram of Oriented Gradients) detectors. This function allows for detecting objects, such as faces, at different sizes (or scales) within an image, which is crucial for dealing with images where objects might appear at different distances from the camera.

**8)cam.release()**--
The cam.release() function in OpenCV is used to release the camera or video capture object, freeing up the resources that were being used.

**9)cv2.destroyAllWindows()**--
kills all windows and ends program



