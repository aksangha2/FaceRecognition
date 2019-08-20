import cv2
#read a video stream and display it
#camera object
cam=cv2.VideoCapture(0)
while True:
  ret,frame=cam.read()
  if ret==False:
   print("something went wrong!")
   continue

  key_pressed=cv2.waitKey(1)&0xFF #bitmasking
  if key_pressed==ord('q'): #ord-->ascii value(8 bit)
   break
  cv2.imshow("video title",frame)

cam.release()
cv2.destroyAllWindows()