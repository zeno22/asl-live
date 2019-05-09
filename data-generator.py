import cv2
import numpy as np
import os

# Create the directory structure
if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")
    os.makedirs("data/train/a")
    os.makedirs("data/train/b")
    os.makedirs("data/train/c")
    os.makedirs("data/train/d")
    os.makedirs("data/train/e")
    os.makedirs("data/train/f")
    os.makedirs("data/train/g")
    os.makedirs("data/train/h")
    os.makedirs("data/train/i")
    os.makedirs("data/train/k")
    os.makedirs("data/train/l")
    os.makedirs("data/train/m")
    os.makedirs("data/train/n")
    os.makedirs("data/train/o")
    os.makedirs("data/train/p")
    os.makedirs("data/train/q")
    os.makedirs("data/train/r")
    os.makedirs("data/train/s")
    os.makedirs("data/train/t")
    os.makedirs("data/train/u")
    os.makedirs("data/train/v")
    os.makedirs("data/train/w")
    os.makedirs("data/train/x")
    os.makedirs("data/train/y")
    
    os.makedirs("data/test/a")
    os.makedirs("data/test/b")
    os.makedirs("data/test/c")
    os.makedirs("data/test/d")
    os.makedirs("data/test/e")
    os.makedirs("data/test/f")
    os.makedirs("data/test/g")
    os.makedirs("data/test/h")
    os.makedirs("data/test/i")
    os.makedirs("data/test/k")
    os.makedirs("data/test/l")
    os.makedirs("data/test/m")
    os.makedirs("data/test/n")
    os.makedirs("data/test/o")
    os.makedirs("data/test/p")
    os.makedirs("data/test/q")
    os.makedirs("data/test/r")
    os.makedirs("data/test/s")
    os.makedirs("data/test/t")
    os.makedirs("data/test/u")
    os.makedirs("data/test/v")
    os.makedirs("data/test/w")
    os.makedirs("data/test/x")
    os.makedirs("data/test/y")

cv2.imshow('asl', cv2.imread('asl.jpg'))
# Train or test 
mode = 'test'
directory = 'data/'+mode+'/'

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Getting count of existing images
    count = {'count_a': len(os.listdir(directory+"/a")),
             'count_b': len(os.listdir(directory+"/b")),
             'count_c': len(os.listdir(directory+"/c")),
             'count_d': len(os.listdir(directory+"/d")),
             'count_e': len(os.listdir(directory+"/e")),
             'count_f': len(os.listdir(directory+"/f")),
             'count_g': len(os.listdir(directory+"/g")),
             'count_h': len(os.listdir(directory+"/h")),
             'count_i': len(os.listdir(directory+"/i")),
             'count_k': len(os.listdir(directory+"/k")),
             'count_l': len(os.listdir(directory+"/l")),
             'count_m': len(os.listdir(directory+"/m")),
             'count_n': len(os.listdir(directory+"/n")),
             'count_o': len(os.listdir(directory+"/o")),
             'count_p': len(os.listdir(directory+"/p")),
             'count_q': len(os.listdir(directory+"/q")),
             'count_r': len(os.listdir(directory+"/r")),
             'count_s': len(os.listdir(directory+"/s")),
             'count_t': len(os.listdir(directory+"/t")),
             'count_u': len(os.listdir(directory+"/u")),
             'count_v': len(os.listdir(directory+"/v")),
             'count_w': len(os.listdir(directory+"/w")),
             'count_x': len(os.listdir(directory+"/x")),
             'count_y': len(os.listdir(directory+"/y")),}
    
    # Printing the count in each set to the screen
    cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "a : "+str(count['count_a']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "b : "+str(count['count_b']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "c : "+str(count['count_c']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "d : "+str(count['count_d']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "e : "+str(count['count_e']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "f : "+str(count['count_f']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "g : "+str(count['count_g']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "h : "+str(count['count_h']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "i : "+str(count['count_i']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "k : "+str(count['count_k']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "l : "+str(count['count_l']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "m : "+str(count['count_m']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "n : "+str(count['count_n']), (10, 360), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "o : "+str(count['count_o']), (10, 380), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "p : "+str(count['count_p']), (10, 400), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "q : "+str(count['count_q']), (100, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "r : "+str(count['count_r']), (100, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "s : "+str(count['count_s']), (100, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "t : "+str(count['count_t']), (100, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "u : "+str(count['count_u']), (100, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "v : "+str(count['count_v']), (100, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "w : "+str(count['count_w']), (100, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "x : "+str(count['count_x']), (100, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "y : "+str(count['count_y']), (100, 280), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    #cv2.rectangle(frame, (x1, y1), (x2, y2), (255,0,0) ,1)
    
    cv2.rectangle(frame, (399, 60), (639, 300), (255,0,0) ,1)
    
    
    # Extracting the ROI
    roi = frame[60:300,399:639]
    
    roi = cv2.resize(roi, (32, 32)) 
 
    cv2.imshow("Frame", frame)
    
    #_, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)
    #kernel = np.ones((1, 1), np.uint8)
    #img = cv2.dilate(mask, kernel, iterations=1)
    #img = cv2.erode(mask, kernel, iterations=1)
    # do the processing after capturing the image!
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    #_, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    roi = cv2.Canny(roi,100,200)
    cv2.imshow("ROI", roi)
    
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'a/'+str(count['count_a'])+'.jpg', roi)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory+'b/'+str(count['count_b'])+'.jpg', roi)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'c/'+str(count['count_c'])+'.jpg', roi)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(directory+'d/'+str(count['count_d'])+'.jpg', roi)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory+'e/'+str(count['count_e'])+'.jpg', roi)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(directory+'f/'+str(count['count_f'])+'.jpg', roi)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(directory+'g/'+str(count['count_g'])+'.jpg', roi)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory+'h/'+str(count['count_h'])+'.jpg', roi)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(directory+'i/'+str(count['count_i'])+'.jpg', roi)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(directory+'k/'+str(count['count_k'])+'.jpg', roi)
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(directory+'l/'+str(count['count_l'])+'.jpg', roi)
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite(directory+'m/'+str(count['count_m'])+'.jpg', roi)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(directory+'n/'+str(count['count_n'])+'.jpg', roi)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(directory+'o/'+str(count['count_o'])+'.jpg', roi)
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(directory+'p/'+str(count['count_p'])+'.jpg', roi)
    if interrupt & 0xFF == ord('q'):
        cv2.imwrite(directory+'q/'+str(count['count_q'])+'.jpg', roi)
    if interrupt & 0xFF == ord('r'):
        cv2.imwrite(directory+'r/'+str(count['count_r'])+'.jpg', roi)
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite(directory+'s/'+str(count['count_s'])+'.jpg', roi)
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(directory+'t/'+str(count['count_t'])+'.jpg', roi)
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(directory+'u/'+str(count['count_u'])+'.jpg', roi)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(directory+'v/'+str(count['count_v'])+'.jpg', roi)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(directory+'w/'+str(count['count_w'])+'.jpg', roi)
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(directory+'x/'+str(count['count_x'])+'.jpg', roi)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(directory+'y/'+str(count['count_y'])+'.jpg', roi)
cap.release()
cv2.destroyAllWindows()
"""
d = "old-data/test/0"
newd = "data/test/0"
for walk in os.walk(d):
    for file in walk[2]:
        roi = cv2.imread(d+"/"+file)
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
        cv2.imwrite(newd+"/"+file, mask)     
"""
