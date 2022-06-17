import cv2
 
capture = cv2.VideoCapture(0)
 
width= int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

videoWriter= cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))

while (True):
 
    ret, frame = capture.read()
     
    if ret:
        cv2.imshow('video', frame)
        videoWriter.write(frame)
 
    if cv2.waitKey(1) == 27:
        break
 
capture.release()
videoWriter.release()
 
cv2.destroyAllWindows()