import numpy as np
import scipy.io.wavfile as wav

  
def interpolate_linearly(wave_table, index):
    truncated_index = int(np.floor(index)) % wave_table.shape[0]
    next_index = (truncated_index + 1) % wave_table.shape[0]

    next_index_weight = index - truncated_index
    truncated_index_weight = 1 - next_index_weight

    return truncated_index_weight * wave_table[truncated_index] + next_index_weight * wave_table[next_index]

def fade_in_out(signal, fade_length=3000):
    fade_length = min(fade_length, len(signal) // 2)

    fade_in = (1 - np.cos(np.linspace(0, np.pi, fade_length))) * 0.5
    fade_out = np.flip(fade_in)

    signal[:fade_length] *= fade_in
    signal[-fade_length:] *= fade_out.copy()

    return signal

def sawtooth(x):
    return (x + np.pi) / np.pi % 2 -1

def main():
    sample_rate = 44100
    f = 440
    t = 3

    #change between np.sin for Sine Wave and sawtooth for Sawtooth Wave
    waveform = sawtooth

    wavetable_length = 64
    wave_table = np.zeros((wavetable_length,))

    for n in range(wavetable_length):
        wave_table[n] = waveform(2 * np.pi * n / wavetable_length)

    output = np.zeros((t * sample_rate,))

    index = 0
    indexIncrement = f * wavetable_length / sample_rate

    for n in range(output.shape[0]):
        output[n] = interpolate_linearly(wave_table, index)
        index += indexIncrement
        index %= wavetable_length
    
    gain = -20
    amplitude = 10 ** (gain / 20)
    output *= amplitude

    output = fade_in_out(output)
     
    wav.write('saw440HzInterpolatedLinearlyFaded4.wav', sample_rate, output.astype(np.float32))

if __name__== '__main__':
    main()
