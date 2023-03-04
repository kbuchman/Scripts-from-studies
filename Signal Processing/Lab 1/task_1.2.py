import numpy as np
import matplotlib.pyplot as plt

def sinewave(amp, freq, freq_s, t_start, t_end):
    '''
    Return an array with values of a sinewave waveform and display it on a plot.
    '''

    # preparing timelines
    _freq_c = 44100 if 44100 > freq_s else freq_s * 2
    t = np.linspace(t_start, 
                    t_end, 
                    round((abs(t_start) + abs(t_end)) * freq_s) + 1)
    t_c = np.linspace(t_start, 
                      t_end, 
                      round((abs(t_start) + abs(t_end)) * _freq_c) + 1)

    # timelines without endpoint
    #t = np.arange(t_start, t_end, (1 / freq_s))
    #t_c = np.arange(t_start, t_end, (1 / _freq_c))

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
