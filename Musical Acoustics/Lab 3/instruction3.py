import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

c = pd.read_csv('Musical Acoustics\Lab 3\widmo c.txt', sep='	')
e = pd.read_csv('Musical Acoustics\Lab 3\widmo e.txt', sep='	')
g = pd.read_csv('Musical Acoustics\Lab 3\widmo g.txt', sep='	')

all_sounds = [c, e, g]

for df in all_sounds:
    df.columns = ['Frequency', 'Amplitude']

acord = pd.concat(all_sounds).reset_index(drop=True)

acord_sorted = acord.sort_values('Frequency')
acord_sorted['Status'] = 0
amp_sum = acord_sorted['Amplitude'].sum()

acord_sorted_rum = acord_sorted.copy()
peaks_count = 1

while (acord_sorted_rum.Status.value_counts().get(0, 0) != 0):
    max = acord_sorted_rum['Amplitude'].nlargest(peaks_count).min()
    max_freq_idx = acord_sorted_rum.loc[acord_sorted_rum.Amplitude == max, 'Amplitude'].index[0]
    peaks_count += 1
    max_freq = acord_sorted_rum.loc[max_freq_idx, 'Frequency']
    acord_sorted_rum.loc[max_freq_idx, 'Status'] = '1'

    idx = max_freq_idx - 1 
    if max_freq_idx - 1 < 0:
        continue
    current_freq = acord_sorted_rum.loc[idx, 'Frequency']
    while (idx >= 0 and max_freq - current_freq < 15):
        acord_sorted_rum.loc[idx, 'Status'] = '2'
        current_freq = acord_sorted_rum.loc[idx, 'Frequency']
        idx -= 1

    idx = max_freq_idx + 1
    current_freq = acord_sorted_rum.loc[idx, 'Frequency']
    while (idx <= len(acord_sorted_rum) and current_freq - max_freq < 15):
        acord_sorted_rum.loc[idx, 'Status'] = '2'
        current_freq = acord_sorted_rum.loc[idx, 'Frequency']
        idx += 1

    print(acord_sorted_rum.Status.count())


acord_sorted_har = acord_sorted.copy()
peaks_count = 1

while (acord_sorted_har.Status.value_counts().get(0, 0) != 0):
    max = acord_sorted_har['Amplitude'].nlargest(peaks_count).min()
    max_freq_idx = acord_sorted_har.loc[acord_sorted_har.Amplitude == max, 'Amplitude'].index[0]
    peaks_count += 1
    max_freq = acord_sorted_har.loc[max_freq_idx, 'Frequency']
    acord_sorted_har.loc[max_freq_idx, 'Status'] = '1'

    idx = max_freq_idx - 1 
    if max_freq_idx - 1 < 0:
        continue
    current_freq = acord_sorted_har.loc[idx, 'Frequency']
    while (idx >= 0 and max_freq - current_freq < 11):
        acord_sorted_har.loc[idx, 'Status'] = '2'
        current_freq = acord_sorted_har.loc[idx, 'Frequency']
        idx -= 1

    idx = max_freq_idx + 1
    current_freq = acord_sorted_har.loc[idx, 'Frequency']
    while (idx <= len(acord_sorted_har) and current_freq - max_freq < (24.7 * ((4.73 * current_freq) + 1))):
        acord_sorted_har.loc[idx, 'Status'] = '2'
        current_freq = acord_sorted_har.loc[idx, 'Frequency']
        idx += 1

    print(acord_sorted_har.Status.count())


acord_sorted_all = acord_sorted.copy()
peaks_count = 1

while (acord_sorted_all.Status.value_counts().get(0, 0) != 0):
    max = acord_sorted_all['Amplitude'].nlargest(peaks_count).min()
    max_freq_idx = acord_sorted_all.loc[acord_sorted_all.Amplitude == max, 'Amplitude'].index[0]
    peaks_count += 1
    max_freq = acord_sorted_all.loc[max_freq_idx, 'Frequency']
    acord_sorted_all.loc[max_freq_idx, 'Status'] = '1'

    idx = max_freq_idx - 1 
    if max_freq_idx - 1 < 0:
        continue
    current_freq = acord_sorted_all.loc[idx, 'Frequency']
    while (idx >= 0 and max_freq - current_freq < 15):
        acord_sorted_all.loc[idx, 'Status'] = '2'
        current_freq = acord_sorted_all.loc[idx, 'Frequency']
        idx -= 1

    idx = max_freq_idx + 1
    current_freq = acord_sorted_all.loc[idx, 'Frequency']
    while (idx <= len(acord_sorted_all) and current_freq - max_freq < 15):
        acord_sorted_all.loc[idx, 'Status'] = '2'
        current_freq = acord_sorted_all.loc[idx, 'Frequency']
        idx += 1

    idx = max_freq_idx - 1 
    if max_freq_idx - 1 < 0:
        continue
    current_freq = acord_sorted_all.loc[idx, 'Frequency']
    while (idx >= 0 and max_freq - current_freq < 11):
        acord_sorted_all.loc[idx, 'Status'] = '2'
        current_freq = acord_sorted_all.loc[idx, 'Frequency']
        idx -= 1

    idx = max_freq_idx + 1
    current_freq = acord_sorted_all.loc[idx, 'Frequency']
    while (idx <= len(acord_sorted_all) and current_freq - max_freq < (24.7 * ((4.73 * current_freq) + 1))):
        acord_sorted_all.loc[idx, 'Status'] = '2'
        current_freq = acord_sorted_all.loc[idx, 'Frequency']
        idx += 1

    print(acord_sorted_all.Status.count())


print('Where: 1 - leave, 2 - remove')
print('Signal after clearing rumbles:')
print(acord_sorted_rum['Status'].value_counts())
acord_sorted_rum.loc[2, 'Status'] = 0
amp_rum_sum = acord_sorted_rum['Amplitude'].sum()

print('Signal after clearing harshness:')
print(acord_sorted_har['Status'].value_counts())
acord_sorted_har.loc[2, 'Status'] = 0
amp_har_sum = acord_sorted_har['Amplitude'].sum()

print('Signal after clearing both:')
print(acord_sorted_all['Status'].value_counts())
acord_sorted_all.loc[2, 'Status'] = 0
amp_all_sum = acord_sorted_all['Amplitude'].sum()


print(f'Rumbles = {round((amp_rum_sum / amp_sum) * 100, 2)}%')
print(f'Harshness = {round((amp_har_sum / amp_sum) * 100, 2)}%')
print(f'Both = {round((amp_all_sum / amp_sum) * 100, 2)}%')