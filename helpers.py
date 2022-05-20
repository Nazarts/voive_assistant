from speech_recognition_funcs import preprocess_dataset, commands
from tensorflow import keras
import tensorflow as tf
import pyaudio
import wave
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


def play_response(command):
    command_response = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'responses',  f'{command}.wav')

    # define stream chunk
    chunk = 1024

    # open a wav format music
    f = wave.open(command_response, "rb")
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # open stream
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    # read data
    data = f.readframes(chunk)

    # play stream
    while data:
        stream.write(data)
        data = f.readframes(chunk)

        # stop stream
    stream.stop_stream()
    stream.close()

    # close PyAudio
    p.terminate()