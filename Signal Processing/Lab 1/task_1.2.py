import numpy as np
import matplotlib.pyplot as plt

def arange(t_start, t_end, step):
    ar = np.arange(t_start, t_end, step)
    return np.append(ar, ar[-1] + step) if ar[-1] < t_end else ar

def sinewave(amp, freq, freq_s, t_start, t_end):
    '''
    Returns an array with values of a sinewave waveform and displays it on a plot.
    '''

    # preparing timelines
    _freq_c = 44100 if 44100 > freq_s else freq_s * 2

    t = arange(t_start, t_end, (1 / freq_s))
    t_c = arange(t_start, t_end, (1 / _freq_c))

    # generating waveforms
    wave = amp * np.sin(2 * np.pi * freq * t)
    wave_c = amp * np.sin(2 * np.pi * freq * t_c)
    
    # plotting
    plt.plot(t, wave, 'ro',  t_c, wave_c, 'b')
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
