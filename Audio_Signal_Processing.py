# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:15:45 2022

@author: jacqu
"""

import numpy as np
from scipy import fftpack
from matplotlib import pyplot as plt
from scipy.io import wavfile


time_step=0.00002



freq1=5 #5Hz
period1 = 1/freq1
time_vec = np.arange(0, 2, time_step)

sig1 = 1000*(np.sin(2 * np.pi / period1 * time_vec))
plt.figure(figsize=(20,10))
plt.title('5Hz Signal')
plt.ylabel('Amplitude')
plt.xlabel('Time (s)')
plt.plot(time_vec, sig1)


freq2=10 #10Hz
period2 = 1/freq2
time_vec = np.arange(0, 2, time_step)

sig2 = 250*(np.sin(2 * np.pi / period2 * time_vec))
plt.figure(figsize=(20,10))
plt.title('10Hz Signal')
plt.ylabel('Amplitude')
plt.xlabel('Time (s)')
plt.plot(time_vec, sig2)


freq3=45 #100Hz
period3 = 1/freq3
time_vec = np.arange(0, 2, time_step)

sig3 = 500*(np.sin(2 * np.pi / period3 * time_vec))
plt.figure(figsize=(20,10))
plt.title('45Hz Signal')
plt.ylabel('Amplitude')
plt.xlabel('Time (s)')
plt.plot(time_vec, sig3)


# Generate the signal
sig = sig1 + sig2 + sig3
plt.figure(figsize=(60,30))
plt.title('Combined Signals')
plt.ylabel('Amplitude')
plt.xlabel('Time (s)')
plt.plot(time_vec, sig)

# Create .WAV file of combined siganl
wavfile.write('CombinedSignal.wav', 44100, sig.astype(np.int16))

# Compute the power
sig_fft = fftpack.fft(sig)
power = np.abs(sig_fft)**2
sample_freq = fftpack.fftfreq(sig.size, d=time_step)

# Plot the power
plt.figure(figsize=(60, 30))
plt.title('Signal in Frequency Domain')
plt.ylabel('Power')
plt.xlabel('Frequency [Hz]')
plt.xlim(-100,100)
plt.plot(sample_freq, power)

# Find the peak frequency
pos_mask = np.where(sample_freq > 0)
freqs = sample_freq[pos_mask]
peak_freq = freqs[power[pos_mask].argmax()]

# Remove all high frequencies
high_freq_fft = sig_fft.copy()
high_freq_fft[np.abs(sample_freq) > peak_freq] = 0
filtered_sig = fftpack.ifft(high_freq_fft)

# Create .WAV file of combined siganl without high frequencies
wavfile.write('CombinedSignalNoHighFreq.wav', 44100, filtered_sig.astype(np.int16))

# PLot without high frequencies
plt.figure(figsize=(60,30))
plt.title('Original and Filtered Time Domain Signals')
plt.plot(time_vec, sig, label='Original signal')
plt.plot(time_vec, filtered_sig, linewidth=5, label='Filtered signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

# Compute the new power
sig_fft1 = fftpack.fft(filtered_sig)
power = np.abs(sig_fft1)**2
sample_freq = fftpack.fftfreq(filtered_sig.size, d=time_step)

# Plot new power
plt.figure(figsize=(60, 30))
plt.title('Filtered Signal in Frequency Domain')
plt.ylabel('Power')
plt.xlabel('Frequency (Hz)')
plt.xlim(-100,100)
plt.plot(sample_freq, power)