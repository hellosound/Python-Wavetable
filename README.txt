# Wavetable Synthesis Project

Waveform Synthesis in Python

This project demonstrates basic waveform synthesis using NumPy and SciPy. It generates an audio waveform using a wavetable approach, applies linear interpolation, and implements a fade-in and fade-out effect before saving the output as a WAV file.


Features

Implements various waveform types:

Sine wave

Sawtooth wave

Reverse sawtooth wave

Square wave

Pulse wave (with duty cycle control)

Triangle wave

Custom wave (combining sine, sawtooth, and triangle)

Uses a wavetable synthesis approach for efficient waveform generation.

Applies linear interpolation for smoother playback.

Implements fade-in and fade-out effects to reduce audio artifacts.

Saves the generated waveform as a 32-bit floating-point WAV file.


Requirements

Ensure you have Python installed along with the required libraries:

pip install numpy scipy


Usage

Run the script using:

python PythonWavetable.py

This will generate a 440Hz triangle wave, apply interpolation and fading.


Customization

Change the waveform function in main() to generate different wave types.

Modify f to set a different frequency.

Adjust t to change the duration of the sound.

Modify gain to control output amplitude.


SLicense

This project is released under the MIT License.