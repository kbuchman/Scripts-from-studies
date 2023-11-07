import matplotlib.pyplot as plt
import pandas as pd

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

while (acord_sorted['Status'].value_counts()[0] > 0):
    max_freq_idx = acord_sorted['Amplitude'].idxmax()
    max_freq = acord_sorted.loc[max_freq_idx]['Frequency']
    acord_sorted.at[max_freq_idx, 'Status'] = 1

    idx = max_freq_idx - 1
    current_freq = acord_sorted.loc[idx]['Frequency']
    while (max_freq - current_freq < 15 and idx >= 0):
        acord_sorted.at[idx, 'Status'] = 2
        idx -= 1
        current_freq = acord_sorted.loc[idx]['Frequency']

    idx = max_freq_idx + 1
    current_freq = acord_sorted.loc[idx]['Frequency']
    while (current_freq - max_freq < 15 and idx <= len(acord_sorted)):
        acord_sorted.at[idx, 'Status'] = 2
        idx += 1
        current_freq = acord_sorted.loc[idx]['Frequency']
amp_dud_sum = acord_sorted['Amplitude'].sum()

while (acord_sorted['Status'].value_counts()[0] > 0):
    max_freq_idx = acord_sorted['Amplitude'].idxmax()
    max_freq = acord_sorted.loc[max_freq_idx]['Frequency']
    acord_sorted.at[max_freq_idx, 'Status'] = 1

    idx = max_freq_idx - 1
    current_freq = acord_sorted.loc[idx]['Frequency']
    while (max_freq - current_freq < 11 and idx >= 0):
        acord_sorted.at[idx, 'Status'] = 2
        idx -= 1
        current_freq = acord_sorted.loc[idx]['Frequency']

    idx = max_freq_idx + 1
    current_freq = acord_sorted.loc[idx]['Frequency']
    while (current_freq - max_freq < (24.7 * ((4.73 * current_freq) + 1)) and idx <= len(acord_sorted)):
        acord_sorted.at[idx, 'Status'] = 2
        idx += 1
        current_freq = acord_sorted.loc[idx]['Frequency']
amp_szo_sum = acord_sorted['Amplitude'].sum()


while (acord_sorted['Status'].value_counts()[0] > 0):
    max_freq_idx = acord_sorted['Amplitude'].idxmax()
    max_freq = acord_sorted.loc[max_freq_idx]['Frequency']
    acord_sorted.at[max_freq_idx, 'Status'] = 1

    idx = max_freq_idx - 1
    current_freq = acord_sorted.loc[idx]['Frequency']
    while (max_freq - current_freq < 15 and idx >= 0):
        acord_sorted.at[idx, 'Status'] = 2
        idx -= 1
        current_freq = acord_sorted.loc[idx]['Frequency']

    idx = max_freq_idx + 1
    current_freq = acord_sorted.loc[idx]['Frequency']
    while (current_freq - max_freq < 15 and idx <= len(acord_sorted)):
        acord_sorted.at[idx, 'Status'] = 2
        idx += 1
        current_freq = acord_sorted.loc[idx]['Frequency']

while (acord_sorted['Status'].value_counts()[0] > 0):
    max_freq_idx = acord_sorted['Amplitude'].idxmax()
    max_freq = acord_sorted.loc[max_freq_idx]['Frequency']
    acord_sorted.at[max_freq_idx, 'Status'] = 1

    idx = max_freq_idx - 1
    current_freq = acord_sorted.loc[idx]['Frequency']
    while (max_freq - current_freq < 11 and idx >= 0):
        acord_sorted.at[idx, 'Status'] = 2
        idx -= 1
        current_freq = acord_sorted.loc[idx]['Frequency']

    idx = max_freq_idx + 1
    current_freq = acord_sorted.loc[idx]['Frequency']
    while (current_freq - max_freq < (24.7 * ((4.73 * current_freq) + 1)) and idx <= len(acord_sorted)):
        acord_sorted.at[idx, 'Status'] = 2
        idx += 1
        current_freq = acord_sorted.loc[idx]['Frequency']
amp_all_sum = acord_sorted['Amplitude'].sum()

print(f'Dudnienia = {amp_dud_sum / amp_sum}%')
print(f'Dudnienia = {amp_szo_sum / amp_sum}%')
print(f'Dudnienia = {amp_all_sum / amp_sum}%')