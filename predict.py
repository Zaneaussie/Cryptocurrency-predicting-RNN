import cv2
import tensorflow as tf
import pandas as pd

CATEGORIES = ['Buy', 'Sell']

dataset = 'test.csv'
df = pd.read_csv(dataset, names=['time', 'low', 'high', 'open', 'close', 'volume'])
df.set_index("time", inplace=True)
df = df[['close', 'volume']]



print(df)
    
    

#model = tf.keras.models.load_model('models/RNN_Final-01-0.534.model')
#prediction = model.predict([df])
#print(prediction)

