'''
from operator import inv
from re import X
from turtle import xcor
import numpy as np
from scipy.io.wavfile import write

# Example vector (numpy array) representing the sound wave
samplerate = 44_100
vector = (np.sin(2 * np.pi * 10_000 * np.linspace(0, 1, samplerate))
        - np.sin(2 * np.pi * 10_030 * np.linspace(0, 1, samplerate)))
#np.sin(2 * np.pi * 22050 * np.linspace(0, 1, 4*44100)) -  np.sin(2 * np.pi * 22000 * np.linspace(0, 1, 4*44100))

# Save the vector to a WAV file
write('output.wav', samplerate, vector.astype(np.float32))

'''
