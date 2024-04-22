import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

def load_image(img_path):

    img = image.load_img(img_path, target_size=(256, 256))
    img_tensor = image.img_to_array(img)  
    # print(img_tensor)                                       # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    #img_tensor /= 255.                                      # imshow expects values in the range [0, 1]
    return img_tensor

# def load_image(img_data):
#     img_tensor = image.img_to_array(img_data)
#     img_tensor = tf.image.resize(img_tensor, [256, 256])
#     img_tensor = tf.expand_dims(img_tensor, axis=0)
#     return img_tensor

def predict_class(image):
    # Your code for image classification prediction here
    # This could involve loading your trained model and processing the image
    # Return the predicted class label
    class_names = ['Tomato_Bacterial_spot',
    'Tomato_Early_blight',
    'Tomato_Late_blight',
    'Tomato_Leaf_Mold',
    'Tomato_Septoria_leaf_spot',
    'Tomato_Spider_mites_Two_spotted_spider_mite',
    'Tomato__Target_Spot',
    'Tomato__Tomato_YellowLeaf__Curl_Virus',
    'Tomato__Tomato_mosaic_virus',
    'Tomato_healthy']
    
    model = load_model("tomatodiseaseclassifier/model.h5")
    # model.summary()

    #img_path = 'spidermites.jpg'    

    new_image = load_image(image)

    pred = model.predict(new_image)

    # predicted_classes = np.argmax(pred)
    predicted_classes = class_names[np.argmax(pred[0])]
    print("Predicted classes:", predicted_classes)
    return predicted_classes