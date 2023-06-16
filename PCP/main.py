from keras.models import load_model  
import cv2  
import numpy as np

np.set_printoptions(suppress=True)

# Load the model


# Load the labels


camera = cv2.VideoCapture(0)

while True:
    ret, image = camera.read()

    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Print the class name, confidence score to screen output
    try:
        image = cv2.putText(image, className[2:], (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.4, (125, 246, 55), 1)
        image = cv2.putText(image, str(np.round(confidenceScore * 100))[:-2], (10, 50), cv2.FONT_HERSHEY_DUPLEX, 0.4, (125, 246, 55), 1)
    except:
        pass


    cv2.imshow("Webcam Image", image)

    # Make the image a numpy array and reshape it to the models input shape.
    

    # Normalize the image array
    

    # Predict using  the model
    

    # Get className

    # Get confidence score

    keyboardInput = cv2.waitKey(1)

    if keyboardInput == 27:
        break

camera.release()
cv2.destroyAllWindows()