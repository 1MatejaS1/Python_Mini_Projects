import numpy as np
import pandas as pd
import matplotlib.pyplot as plotter
import csv
from scipy.signal import find_peaks

# read in solar irradiance data from Hicks Building, University of Sheffield
url = "https://raw.githubusercontent.com/alastairbuckley/PHY6000/master/ss_testbed_irrad_2012.csv"
data = pd.read_csv(url, parse_dates=["dateandtime"])
# Use the col_mapper dictionary to rename cols
col_mapper = {"dateandtime": "timestamp", "GHI": "ghi", "DHI": "dhi"}
data.rename(columns=col_mapper, inplace=True)
# Set the timestamp as the index of the dataframe
data.set_index("timestamp", inplace=True)
# Tell pandas our timestamps are UTC
data = data.tz_localize(tz="UTC")
data2 = data.to_numpy() #convert number data to numpy 2d array
ghi_data, dhi_data=np.split(data2,2,axis=1) #split ghi and dhi data
ghi_data_2 = ghi_data.flatten() #flatten to 1d
dhi_data_2 = dhi_data.flatten() #flatten to 1d
time = np.arange(0,len(ghi_data)*2,2) #create a new time array with 2 minute increments
samplingFrequency = 1/(time[1]-time[0])
print(samplingFrequency)

# Create subplots
figure, axis = plotter.subplots(2, 1)
plotter.subplots_adjust(hspace=0.5)

# Plot f(t)

axis[0].set_xlim([1,(len(time))]) # time limits for the plot of the audio signal
axis[0].plot(time, ghi_data_2, label='GHI')
axis[0].set_xlabel('Time [s]')
axis[0].set_ylabel('Irradiance [W/m^2]')
# Fourier transform calculation if F(f)
fourierTransform = np.fft.fft(ghi_data_2)/len(ghi_data_2)           # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(ghi_data_2)/2))] # Exclude sampling frequency
tpCount     = len(ghi_data_2)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency
frequencies = values/timePeriod

# Plot f(t)_2
axis[0].set_title('Original Irradiance Value', fontname="EB Garamond", fontsize = 25)
axis[0].set_xlim([1,(len(time))]) # time limits for the plot of the audio signal
axis[0].plot(time, dhi_data_2, label='DHI')
axis[0].set_xlabel('Time [minutes]', fontname="EB Garamond", fontsize = 17)
axis[0].set_ylabel('Irradiance [W/m^2]', fontname="EB Garamond", fontsize = 17)
axis[0].legend(loc="upper left")


axis[0].xaxis.set_tick_params(labelsize=14)
axis[0].yaxis.set_tick_params(labelsize=12)

# Fourier transform calculation if F(f)_2
fourierTransform2 = np.fft.fft(dhi_data_2)/len(dhi_data_2)           # Normalize amplitude
fourierTransform2 = fourierTransform2[range(int(len(dhi_data_2)/2))] # Exclude sampling frequency
tpCount2     = len(dhi_data_2)
values2      = np.arange(int(tpCount2/2))
timePeriod2  = tpCount2/samplingFrequency
frequencies2 = values2/timePeriod2


# Plot F(f) and F(t)_2
axis[1].set_title('Fourier transform', fontname="EB Garamond", fontsize = 22)
axis[1].set_xlim([-0.00005,0.002]) # frequency limits for the plot of the Fourier transform
#axis[1].set_ylim([0,0.05])
#axis[1].set_xtics(range(1/min(values)*60,1/max(values)*60))
axis[1].plot(frequencies, abs(fourierTransform), label='GHI')
axis[1].plot(frequencies2, abs(fourierTransform2), label='DHI')

realFourier = abs(fourierTransform)
peaks = find_peaks(realFourier, height = 10, threshold = 1, distance = 1)
height = peaks[1]['peak_heights'] #list of the heights of the peaks
peak_pos = frequencies[peaks[0]] #list of the peaks positions
axis[1].scatter(peak_pos, height, color = 'k', s = 25, marker = 'x', label = 'Maxima')

axis[1].legend()
axis[1].set_xlabel('Frequency [1/minute]', fontname="EB Garamond", fontsize = 17)
axis[1].set_ylabel('Irradiance [W/m^2]', fontname="EB Garamond", fontsize = 17)

axis[1].xaxis.set_tick_params(labelsize=14)
axis[1].yaxis.set_tick_params(labelsize=12)

plotter.savefig('Irradiance.png', dpi=1000)

plotter.show()

#optional:
#print(len(time))
#print(height)
#print(peak_pos)

freq_in_hours = (1/peak_pos[2])/60
irr_hourly = height[2]

freq2_in_hours = (1/peak_pos[5])/60
irr2_hourly = height[5]

print("Irradiance magnitude:",round(irr_hourly,2),"W/m^2, at:",round(freq_in_hours,2),"hours")
print("Irradiance magnitude:",round(irr2_hourly,2),"W/m^2, at:",round(freq2_in_hours,2),"hours")

average1 = np.average(ghi_data_2)
print(round(average1,2)) #this result neglects the zeros in the time 
