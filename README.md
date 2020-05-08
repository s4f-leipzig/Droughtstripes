# DROUGHTSTRIPES (Duerrestreifen)

Droughtstripes show the precipitation anomaly for each year (or a specific month of a year) in comparison to the reference period (here: 1971 - 2000). The idea is based on the warming stripes invented by Ed Hawkins (https://showyourstripes.info/faq) and shall show the effects of the climate crisis on precipitation.

This code creates droughtstipes from data of the Deutsche Wetterdienst (DWD) for a selectable month of the year. You can chose to create a plot for as many federal states as you want or for the whole country.

## Example
Droughtstripes for Germany and for each April in 1881 - 2020, brown = negative anomaly (less precipitation than average), turquoise = positive anomaly (more precipitation than average).
![Droughtstripes for April 1881 - 2020 for Germany](https://github.com/s4f-leipzig/Droughtstripes/blob/master/stripes_Deutschland_04_1881-2020.jpg)

## Prerequisits
The code is written in Python3 but can be easily adjusted to Python2.7 (see line 37 of the code for information)

## Required Python Packages
numpy  
matplotlib  
pandas  
urllib  


## Manual Adjustments To Be Made When Using This Code
### Mandatory
1. chose month you want to plot (line 18)
2. chose local file path to store raw data as txt-file (line 20)
3. chose federal states you want to plot (line 71) by adding the number of the state according to dictionary (lines 62-67)

### Not Mandatory Adjustments, Just To Play Around
1. adjust colorbar by changing colors in function custom_div_cmap or use a predifined colorbar from matplotlib
2. adjust reference period to see how this changes the anomalies
3. adjust the limits of the colorbar by chosing different standard deviations


## Authors
Scientists for Future Leipzig
