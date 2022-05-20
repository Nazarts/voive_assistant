from speech_recognition_funcs import preprocess_dataset, commands
from tensorflow import keras
import tensorflow as tf
import matplotlib.pyplot as plt
import os

# Audio recognition wrapper
def sample_recognition():
    sample_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'recordedFile.wav')

    print(os.path.dirname(os.path.realpath(__file__)))

    sample_ds = preprocess_dataset([str(sample_file)])

    model = keras.models.load_model('model_weights/my_h5_model.h5')

    for spectrogram, label in sample_ds.batch(100):
        prediction = model(spectrogram)

        results = tf.nn.softmax(prediction[0])

    return commands[tf.argmax(results).numpy()]