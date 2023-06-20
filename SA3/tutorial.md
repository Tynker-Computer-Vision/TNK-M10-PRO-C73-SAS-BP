Load the Module
================

In this activity, you will learn to make predictions using the model.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10563421/explore-color.gif" width = "480" height = "320">

Follow the given steps to complete this activity:

1. Resize the images

* Open the main.py file.    

*  Display the `class name`, `confidence score` using  `cv2.putText()` to screen output.

    try:
        image = cv2.putText(image, class_name[2:], (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.4, (125, 246, 55), 1)
        image = cv2.putText(image, str(np.round(confidence_score * 100))[:-2], (10, 50), cv2.FONT_HERSHEY_DUPLEX, 0.4, (125, 246, 55), 1)
    except:
        pass
        

* Use model to predict the output for current image.

    `prediction = model.predict(image)`

* Use `np.argmax` to find a index with highest value in prediction array.

    `index = np.argmax(prediction)`

* Use the index to get the name from `class_names`.

    `class_name = class_names[index]`

* Get `confidence_score` from `prediction[0]` at index.

    `confidence_score = prediction[0][index]`


* Save and run the code to check the output.
