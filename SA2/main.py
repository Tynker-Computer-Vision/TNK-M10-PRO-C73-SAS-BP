import cv2  
import numpy as np
from keras.models import load_model  

model = load_model("keras_Model.h5", compile=False)

class_names = open("labels.txt", "r").readlines()

camera = cv2.VideoCapture(0)

while True:
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels

    cv2.imshow("Webcam Image", image)
 
    # Make the image a numpy array and reshape it to the models input shape.

    # Print original image
    

    # Normalize the image array
    
    
    # Print normalized image
    

    keyboard_input = cv2.waitKey(1)
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()
