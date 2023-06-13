import cv2  
import numpy as np
from keras.models import load_model  

model = load_model("keras_Model.h5", compile=False)

class_names = open("labels.txt", "r").readlines()

camera = cv2.VideoCapture(0)

while True:
    ret, image = camera.read()

    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Print the class name, confidence score to screen output
    

    cv2.imshow("Webcam Image", image)
 
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    image = (image / 127.5) -1

    # Use model to pridict the output for current image
    
    # Use np.argmax to find a index with highest value in prediction array
    
    # Use the index to get the name from class_names
    
    # Get confidence_score from prediction[0] at index 
    

    keyboard_input = cv2.waitKey(1)
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()
