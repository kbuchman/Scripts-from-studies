# script used for creating data of waveforms based on SPL measurements

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# calculates wave amplidude [Pa] from SPL [dB]
def amp(a):
    return np.sqrt(2) * abs(np.power(10, ((a / 20) - 5 + np.log10(2)))) 

# component waves params
f = 2000    # [Hz]
spl = 74.5    # [dB]
# phase shift values
fi = [0, 180]   # [∘]
w = 2 * np.pi * f

# SPL values of the wave resulting from the interference
i_spl = [80.2, 73.8]

if len(fi) != len(i_spl):
    print('Invalid amount of data!')
    os._exit(0)

# waveform params
start = 0
end = 2 / f
samples = 2000

# setting up first wave
x = np.linspace(start, end, samples)
y = amp(spl) * np.sin(w * x)

# setting up rest of waves
for i, am in enumerate(i_spl):
    y1 = amp(spl) * np.sin(w * x + ((fi[i] * np.pi) / 180))    # second component wave with fi phase shift
    yi = amp(am) * np.sin(w * x)    # the wave resulting from the interference

    # saving to csv
    df = pd.DataFrame({'x': x, 'y': y, 'y1' : y1, 'yc' : yi})
    df.to_csv(f'data{i}.csv', index=False, sep='\t')


# plot for checking if everything is all right
plt.plot(x, y, 'b', x, y1, 'r', x, yi, 'g')
plt.show()