import numpy as np
from keras.models import model_from_json
import operator
import cv2
import sys, os

# Loading the model
json_file = open("model-asl-bw.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
# load weights into new model
loaded_model.load_weights("model-asl-bw.h5")
print("Loaded model from disk")

cap = cv2.VideoCapture(0)
cv2.imshow('asl', cv2.imread('asl.jpg'))
# Category dictionary
categories = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h',8: 'i', 9: 'k', 10: 'l', 11: 'm', 12: 'n', 13: 'o', 14: 'p', 15: 'q', 16: 'r', 17: 's', 18: 't', 19: 'u', 20: 'v', 21: 'w', 22: 'x', 23: 'y'}

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    cv2.rectangle(frame, (399, 60), (639, 300), (255,0,0) ,1)
    # Extracting the ROI
    roi = frame[60:300,399:639]
    
    # Resizing the ROI so it can be fed to the model for prediction
    roi = cv2.resize(roi, (32, 32)) 
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    test_image = cv2.Canny(roi,100,200)
    #_, test_image = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("test", test_image)
    # Batch of 1
    result = loaded_model.predict(test_image.reshape(1, 32, 32, 1))
    prediction = {'a': result[0][0], 
                  'b': result[0][1], 
                  'c': result[0][2],
                  'd': result[0][3],
                  'e': result[0][4],
                  'f': result[0][5],
                  'g': result[0][6],
                  'h': result[0][7],
                  'i': result[0][8],
                  'k': result[0][9],
                  'l': result[0][10],
                  'm': result[0][11],
                  'n': result[0][12],
                  'o': result[0][13],
                  'p': result[0][14],
                  'q': result[0][15],
                  'r': result[0][16],
                  's': result[0][17],
                  't': result[0][18],
                  'u': result[0][19],
                  'v': result[0][20],
                  'w': result[0][21],
                  'x': result[0][22],
                  'y': result[0][23]
                  }
    # Sorting based on top prediction
    prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
    print(prediction)
    # Displaying the predictions
    cv2.putText(frame, prediction[0][0], (10, 120), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,255), 2)    
    cv2.imshow("Frame", frame)
    
    interrupt = cv2.waitKey(20)
    if interrupt & 0xFF == 27: # esc key
        break
        
 
cap.release()
cv2.destroyAllWindows()
