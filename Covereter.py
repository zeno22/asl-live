import numpy as np
import cv2

cap = cv2.VideoCapture('#.mov')


success,roi = cap.read()
count = 0
success = True
while success:
  success,roi = cap.read()
  roi = cv2.flip(roi, 1)
  roi = cv2.resize(roi, (32, 32))
  roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
  roi = cv2.Canny(roi,100,200)
  #cv2.imshow('img',image)

  cv2.imshow('edges',roi)
  #number=np.sum(edges.ravel())/200000
  #print(number)
  cv2.imwrite("C:/Users/admin/.spyder-py3/Project/d/%d.jpg" % count, roi) 
  #cv2.imwrite("C:/Users/admin/.spyder-py3/Project/color/bgframe%d.jpg" % count, region_of_interest) 
  #cv2.imwrite("C:/Users/admin/.spyder-py3/Project/edge/bgframe%d.jpg" % count, edges) 
    # save frame as JPEG file
  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1
  

cap.release()
cv2.destroyAllWindows()