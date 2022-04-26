from tensorflow.keras.applications.xception import Xception
from tensorflow.keras.utils import plot_model
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.applications.xception import preprocess_input
from tensorflow.keras.applications.xception import decode_predictions


model = Xception(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
)
model.summary()

image1 = image.load_img(
    "static/3ca3283110bf430ebdfd7b8f7b02e9ed.jpeg", target_size=(299, 299))
print(image1.size)

transformedImage = image.img_to_array(image1)
print(transformedImage.shape)

transformedImage = np.expand_dims(transformedImage, axis=0)
print(transformedImage.shape)

transformedImage = preprocess_input(transformedImage)
print(transformedImage)

prediction = model.predict(transformedImage)
print(prediction)


predictionLabel = decode_predictions(prediction, top=5)
print("predictionLabel---------->", predictionLabel)
