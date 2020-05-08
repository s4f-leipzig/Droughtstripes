#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 4 13:03:43 2020

@author: Scientists4Future Leipzig
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import urllib 
from matplotlib.colors import LinearSegmentedColormap


## Manual entries required: 
# Enter number of month to plot - add '0' before months with one digit
month = "04"
# Enter your local path and filename where to save the raw data
local ="regional_averages_rr_"+month+".txt"


## Definition of manual colormap:
# create colormap
def custom_div_cmap(numcolors=256, name='custom_div_cmap',colors=['saddlebrown','chocolate','white','darkturquoise','darkcyan']):
    """ Create a custom colormap
 	Colors can be specified in any way understandable by matplotlib.colors.ColorConverter.to_rgb() 
 	-> https://matplotlib.org/3.1.0/gallery/color/named_colors.html
    """
    cmap = LinearSegmentedColormap.from_list(name=name, colors=colors, N=numcolors)
    return cmap


### RETRIEVE DATA FROM DWD 
#link to DWD-ftp server
link = "ftp://ftp-cdc.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation/regional_averages_rr_"+month+".txt"
#retrieve data and cleanup !for Python2.7 comment out lines 39, 40 and uncomment lines 41, 42
precip_raw = urllib.request.urlretrieve(link, local)
urllib.request.urlcleanup()
#precip_raw = urllib.urlretrieve(link, local)
#urllib.urlcleanup()
#read in the data as pandas table
data = pd.read_table(precip_raw[0],skiprows=1, sep=';')


#### SOME SPECIFICATIONS BEFORE PLOTTING
# reference period for mean calculation 1971 - 2000 according to warming stripes by Ed Hawkins (see https://showyourstripes.info/faq)
ref_min = 1971
ref_max = 2000

#select the data during the refence period
ref_data = data[(data['Jahr']>=ref_min) & (data['Jahr']<=ref_max)]

#reference period for the standard deviation, also ccording to the original warming stripes
ref_min_std = 1901
ref_max_std = 2000

#select the data during the std ref period
ref_data_std = data[(data['Jahr']>=ref_min_std) & (data['Jahr']<=ref_max_std)]

# a dictionary for the quick selection of a federal state or whole Germany by number
regio = {1:'Sachsen',2:'Deutschland',3:'Brandenburg/Berlin', 4:'Brandenburg',
       5:'Baden-Wuerttemberg', 6:'Bayern', 7:'Hessen', 8:'Mecklenburg-Vorpommern',
       9:'Niedersachsen', 10:'Niedersachsen/Hamburg/Bremen',
       11:'Nordrhein-Westfalen', 12:'Rheinland-Pfalz', 13:'Schleswig-Holstein',
       14:'Saarland', 15:'Sachsen-Anhalt',
       16:'Thueringen/Sachsen-Anhalt', 17:'Thueringen'}

### PLOTTING OF DROUGHTSTRIPES
#select the federal state you want to plot, numbers according to dictionary above, here: Sachsen, Deutschland
regio_lst=[1,2]
#loop through selected states and create a plot for each
for reg in regio_lst: 
    region = regio[reg] 
    # calculate the standard deviation for the period definded above
    std = ref_data_std[region].std()
    #select temperature in the region
    temps_region = data[region]
    
    # calculate the precipitation anomaly i.e. deviation from defined mean of ref period
    temps = temps_region - ref_data[region].mean()
    ## stack data to be able to plot them with imshow
    stacked_temps = np.stack((temps, temps))
    
    #min and max values for the colormap !this value deviates from the warming stripes where a standard deviation of +/-2.6 was chosen
    vmin = -1.7*std 
    vmax = 1.7*std 
    
    ## plotting
    fig = plt.figure(figsize=(16,9)) #adjust figsize, for example for cubic figure
    #plot the image, with manual color bar defined above in custom_div_cmap function
    cmap = custom_div_cmap()
    img = plt.imshow(stacked_temps, cmap=cmap, aspect='auto', vmin=vmin, vmax=vmax, interpolation='none')
    #this just turns all labels, axis etc off so that there are only the stripes
    plt.gca().set_axis_off()
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    #save in your desired directory
    plt.savefig("stripes_"+temps.name+'_'+month+'_'+str(data['Jahr'].min())+'-'+str(data['Jahr'].max())+".jpg", bbox_inches = 'tight', pad_inches = 0, dpi=300)