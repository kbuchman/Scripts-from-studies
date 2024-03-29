import pandas as pd
import numpy as np
import wavio
import librosa

c = pd.read_csv('Musical Acoustics\Lab 3\widmo c.txt', sep='	')
e = pd.read_csv('Musical Acoustics\Lab 3\widmo e.txt', sep='	')
g = pd.read_csv('Musical Acoustics\Lab 3\widmo g.txt', sep='	')

all_sounds = [c, e, g]

for df in all_sounds:
    df.columns = ['Frequency', 'Amplitude']

acord = pd.concat(all_sounds).reset_index(drop=True)

acord['Index'] = acord.index
acord_sorted = acord.sort_values('Frequency', ascending=False)
acord_sorted['Status'] = 0
amp_sum = acord_sorted['Amplitude'].sum()

acord_sorted_rum = acord_sorted.copy()

last_peak_freq = acord_sorted_rum.Frequency[acord_sorted_rum.Amplitude.idxmax()]
for i, freq in enumerate(acord_sorted_rum.Frequency):
    if freq - last_peak_freq > 15:
        last_peak_freq = freq
        acord_sorted_rum.Status[i] = 1
        continue
    elif  freq - last_peak_freq < 0:
        acord_sorted_rum.Status[i] = 1
        continue
    acord_sorted_rum.Status[i] = 2


acord_sorted_har = acord_sorted.copy()                  

last_peak_freq = acord_sorted_har.Frequency[0] + 11
for i, freq in enumerate(acord_sorted_har.Frequency):
    if abs(last_peak_freq - freq) >= 11:
        erb = .25 * 24.7 * ((4.37 * last_peak_freq * 1000) + 1)
        acord_sorted_har.Status[i] = 2

        if abs(last_peak_freq - freq) < erb:
            last_peak_freq = freq
            continue
    acord_sorted_har.Status[i] = 1
    #print(acord_sorted_har.Status.value_counts())


acord_sorted_all = acord_sorted_har.copy()
acord_sorted_all['Amplitude'].mask(acord_sorted_all['Status'] == 2, 0, inplace=True)
acord_sorted_all.Status[:] = 0

last_peak_freq = acord_sorted_all.Frequency[0] + 16
for i, freq in enumerate(acord_sorted_all.Frequency):
    if abs(last_peak_freq - freq) > 15:
        last_peak_freq = freq
        acord_sorted_all.Status[i] = 1
        continue
    acord_sorted_all.Status[i] = 2

print(acord_sorted_all.Status.value_counts())

print('Group: Karol Buchman and Paweł Procki')
print('Where: 1 - leave, 2 - remove')
print('Signal after clearing rumbles:')
print(acord_sorted_rum['Status'].value_counts())
acord_sorted_rum['Amplitude'].mask(acord_sorted_rum['Status'] == 2, 0, inplace=True)
amp_rum_sum = acord_sorted_rum['Amplitude'].sum()

print('Signal after clearing harshness:')
print(acord_sorted_har['Status'].value_counts())
acord_sorted_har['Amplitude'].mask(acord_sorted_har['Status'] == 2, 0, inplace=True)
amp_har_sum = acord_sorted_har['Amplitude'].sum()

print('Signal after clearing both:')
print(acord_sorted_all['Status'].value_counts())
acord_sorted_all['Amplitude'].mask(acord_sorted_all['Status'] == 2, 0, inplace=True)
amp_all_sum = acord_sorted_all['Amplitude'].sum()


print(f'Rumbles = {round((1 - amp_rum_sum / amp_sum) * 100, 2)}%')
print(f'Harshness = {round((1 - amp_har_sum / amp_sum) * 100, 2)}%')
print(f'Both = {round((1 - amp_all_sum / amp_sum) * 100, 2)}%')

y, fs = librosa.load(r'Musical Acoustics\Lab 3\akord.wav')
duration = librosa.get_duration(y=y, sr=fs)


def generate_audio(frequencies, amplitudes, duration, sample_rate):
    time = np.arange(0, duration, 1 / sample_rate)
    audio_signal = np.zeros_like(time)

    for freq, amp in zip(frequencies, amplitudes):
        audio_signal += amp * np.sin(2 * np.pi * freq * time)

    return audio_signal

acord_sorted_rum = acord_sorted_rum.sort_values('Index')
acord_sorted_har = acord_sorted_har.sort_values('Index')
acord_sorted_all = acord_sorted_all.sort_values('Index')

wavio.write("without_rumbles.wav", generate_audio(acord_sorted_rum.Frequency, acord_sorted_rum.Amplitude, duration, fs), fs, sampwidth=3)
wavio.write("without_harshness.wav", generate_audio(acord_sorted_har.Frequency, acord_sorted_har.Amplitude, duration, fs), fs, sampwidth=3)
wavio.write("without_both.wav", generate_audio(acord_sorted_all.Frequency, acord_sorted_all.Amplitude, duration, fs), fs, sampwidth=3)