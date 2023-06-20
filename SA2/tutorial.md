Load the Module
================

In this activity, you will learn to load the module and resize and normalize the images.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10539193/image.png" width = "380" height = "420">

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10539195/image2.png" width = "380" height = "420">

Follow the given steps to complete this activity:

1. Resize and normalize the images

* Open the main.py file.

* Resize the raw image using `cv2.resize()` function to `height 224 pixels` and `width 224 pixels`.

    `image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)`
        

* Make the image a numpy array and reshape it to the models input shape.

    `image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)`

* Print original image.

   `print(image)`

    `cv2.waitKey(0)`

* Normalize the image array.

    `image = (image / 127.5) -1`
    
* Print normalized image.

    `print(image)`

    `cv2.waitKey(0)`

* Save and run the code to check the output.
