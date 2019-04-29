# -*- coding: utf-8 -*-
"""run_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11qYHSM1OZp6QU1UqfY3MulCJZ_0y8uYa
"""

import tensorflow as tf
from tensorflow import keras
import os
import numpy as np

tf.__version__

checkpoint_path = "cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Import the class names to translate the model output from an index to a meaninful class name
class_names = ['cake', 'traffic_light', 'donut', 'book', 'wheel', 'wristwatch', 'laptop', 'sun', 'shovel', 'drums', 'bicycle', 'cactus', 'broom', 'crown', 'car', 'clock']

# This function has the information necessary to create a model with the appropriate dimensions
def create_model():
  model = tf.keras.models.Sequential([
      keras.layers.Dense(512, activation=tf.keras.activations.relu, input_shape=(784,)),
      keras.layers.Dropout(0.2),
      keras.layers.Dense(16, activation=tf.keras.activations.softmax)
  ])
  
  model.compile(optimizer=tf.keras.optimizers.Adam(),
                loss=tf.keras.losses.sparse_categorical_crossentropy,
                metrics=['accuracy'])
  
  return model


# To run the model we already trained, we must create a new model with the same parameters and load the trained weights
res_model = create_model()
res_model.load_weights(checkpoint_path) #load weights from folder

# replace this sample with actual array of size (1,784)
sample = np.array(np.random.randint(255, size=784)) / 255 
sample = sample.reshape(1, 784)

# Run the restored model on the sample image, output an index
Y_idx = int(np.argmax(res_model.predict(sample)))
# translate the index to a class name
predicted_class = class_names[Y_idx]
print(predicted_class)
