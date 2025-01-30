import numpy as np
import scipy.io.wavfile as wav

def interpolate_linearly(wave_table, index):
    truncated_index = int(np.floor(index))
    
    def interpolate_linearly(wave_table, index):
        truncated_index = int(np.floor(index))
        next_index = (truncated_index + 1) % wave_table.shape[0]
    
        next_index_weight = index - truncated_index
        truncated_index_weight = 1 - next_index_weight

        return truncated_index_weight * wave_table[truncated_index] + next_index_weight * wave_table[next_index]
    
def main():
    sample_rate = 44100
    f = 440
    t = 3
    wavetable_length = 64
    wave_table = np.zeros((wavetable_length,))

    for n in range(wavetable_length):
        wave_table[n] = np.sin(2 * np.pi * n / wavetable_length)

    output = np.zeros((t * sample_rate,))

    index = 0
    indexIncrement = f * wavetable_length / sample_rate

    for n in range(output.shape[0]):
        output[n] = interpolate_linearly(wave_table, index)
        index += indexIncrement
    
    gain = -20
    amplitude = 10 ** (gain / 20)
    output *= amplitude
    
    wav.write('sine440HzInterpolatedLinearly.wav', sample_rate, output.astype(np.float32))

if __name__== '__main__':
    main()
