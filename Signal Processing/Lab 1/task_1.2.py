import numpy as np
import matplotlib.pyplot as plt

def sinewave(amp, freq, freq_s, t_start, t_end):
    # preparing timelines
    t = np.arange(t_start, t_end, (1 / freq_s))
    t44100 = np.arange(t_start, t_end, (1 / 44100))

    # generating waveforms
    wave = amp * np.sin(2 * np.pi * freq * t)
    wave44100 = amp * np.sin(2 * np.pi * freq * t44100)
    
    # plotting
    plt.plot(t, wave, 'ro',  t44100, wave44100, 'b')
    plt.title(f'Sine function (amount of periods: {(abs(t_start) + abs(t_end)) / (1 / freq)})')
    plt.xlabel('Time, s')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()

    return wave

def main():
    x = sinewave(2, 2, 6, -2, 1)
    print(x)

if __name__ == '__main__':
    main()