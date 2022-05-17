from speech_recognition_funcs import preprocess_dataset, commands
from tensorflow import keras
import tensorflow as tf
import matplotlib.pyplot as plt

sample_file = r'C:\Users\nazik\PycharmProjects\voive_assistant\recordedFile.wav'

sample_ds = preprocess_dataset([str(sample_file)])

model = keras.models.load_model('model_weights/my_h5_model.h5')

for spectrogram, label in sample_ds.batch(100):
  prediction = model(spectrogram)
  plt.bar(commands, tf.nn.softmax(prediction[0]))
  plt.title(f'Predictions for "{commands[label[0]]}"')
  plt.show()