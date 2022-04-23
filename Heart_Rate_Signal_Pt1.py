# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 22:06:09 2022

@author: jacqu
"""
# Import Packages
import heartpy as hp
import matplotlib.pyplot as plt

sample_rate = 300

data=hp.get_data('108_Output_mono.csv')
plt.figure(figsize=(12,4))
plt.plot(data, color='purple')
plt.title("Heart Rate Frequency Signal")
plt.show

# Run Analysis
wd, m = hp.process(data, sample_rate)

# Visualise in plot of custom size
plt.figure(figsize=(3,4))
hp.plotter(wd, m)

#Display Computed Measures
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))
    
