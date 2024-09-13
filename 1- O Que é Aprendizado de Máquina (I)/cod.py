x = [-1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 8.0, 10.0, 15.0]

y = []
for num in x:
    y.append((num*6)-(num-3))

print(y)
#y = [-2.0, 3.0, 8.0, 13.0, 18.0, 23.0, 43.0, 53.0, 78.0]

import tensorflow as tf
from tensorflow import keras
import numpy as np

model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

x = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 8.0, 10.0, 15.0], dtype=float)
y = np.array([-2.0, 3.0, 8.0, 13.0, 18.0, 23.0, 43.0, 53.0, 78.0], dtype=float)

model.fit(x,y, epochs=500)

print(model.predict([12.0]))