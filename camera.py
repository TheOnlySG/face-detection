import cv2  # Importing the OpenCV library for computer vision tasks

# Initializing the camera using VideoCapture. 0 is the default camera.
cam = cv2.VideoCapture(0)

# Creating a named window where the webcam feed will be displayed.
cv2.namedWindow("python webcam Screenshot App")

# Initializing the screenshot counter to 0. This will be used to name the screenshots taken.
img_counter = 0

# Informing the user about the key controls for taking screenshots and exiting the program.
print("You can press the space bar to capture an image and ESC to exit the program.")

# Starting an infinite loop to continuously capture frames from the webcam
while True:
    # Capturing frame-by-frame from the webcam
    ret, frame = cam.read()
    
    # If frame capture fails (e.g., if the camera is unavailable), print an error and break the loop
    if not ret:
        print("Failed to grab frame")
        break
    
    # Displaying the current frame in the "Camera" window
    cv2.imshow("Camera", frame)
    
    # Waiting for the user to press a key. WaitKey(1) checks for key presses every 1 millisecond
    k = cv2.waitKey(1)
    
    # Checking if the Escape key (ASCII 27) is pressed
    if k % 256 == 27:
        print("You pressed the Escape key, the program is now closing.")
        print("Thank you! :)")
        break
    
    # Checking if the spacebar (ASCII 32) is pressed to capture an image
    elif k % 256 == 32:
        # Defining the filename for the image using the current img_counter value
        image_name = "opencv_frame_{}.png".format(img_counter)
        
        # Saving the current frame (screenshot) as a PNG file
        cv2.imwrite(image_name, frame)
        
        # Informing the user that the screenshot has been taken
        print("Image Captured And Saved to the same folder as this program.")
        
        # Increment the counter to create a unique filename for the next screenshot
        img_counter += 1

# Releasing the camera after exiting the loop
cam.release()

# Destroying all OpenCV windows opened by the program
cv2.destroyAllWindows()
