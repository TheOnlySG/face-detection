import cv2
cam =  cv2.VideoCapture(0)
cv2.namedWindow("python webcam Screenshot App")
img_counter = 0
print("you can press space bar to capture image and esc to exit the program.")
while True:
    ret,frame = cam.read()
    if not ret:
        print("failed to gram frame")
        break
    cv2.imshow("Camera",frame)
    k= cv2.waitKey(1)
    if k%256 == 27:
        print("You Pressed the Escape key,the program is now closing.")
        print("thankyou ! :)")
        break
    elif  k%256 == 32:
        image_name= "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(image_name, frame)
        print("screenshot taken")
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
