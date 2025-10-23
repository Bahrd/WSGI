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

from midiutil import MIDIFile
from scipy.io.wavfile import write, read

# Tworzenie pliku MIDI z jedną ścieżką
midi = MIDIFile(1)
track = 0
time = 0
channel = 0
volume = 100
duration = 1  # długość nuty w taktach

midi.addTrackName(track, time, "Melodic Minor Scale")
midi.addTempo(track, time, 120)

# Wznosząca skala melodyczna molowa (A melodic minor ascending)
ascending = [69, 71, 72, 74, 76, 78, 80, 81]  # A B C D E F# G# A

# Opadająca skala naturalna molowa (A natural minor descending)
descending = [81, 79, 77, 76, 74, 72, 71, 69]  # A G F E D C B A

# Dodajemy nuty wznoszące
for i, pitch in enumerate(ascending):
    midi.addNote(track, channel, pitch, time + i, duration, volume)

# Dodajemy nuty opadające
offset = len(ascending)
for i, pitch in enumerate(descending):
    midi.addNote(track, channel, pitch, time + offset + i, duration, volume)

# Zapisujemy plik MIDI
with open("skala_molowa_melodyczna.mid", "wb") as output_file:
    midi.writeFile(output_file)
