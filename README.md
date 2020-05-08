#DROUGHTSTRIPES (Duerrestreifen)

Droughtstripes show the precipitation anomaly for each year (or a specific month of a year) in comparison to the reference period (here: 1971 - 2000). The idea is based on the warming stripes created by Ed Hawkins ([https://showyourstripes.info/faq]) and shall show the effects of the climate crisis on precipitation.

This code creates droughtstipes from data of the Deutsche Wetterdienst (DWD) for a selectable month of the year. You can chose to create a plot for as many federal states as you want or for the whole country.
#EXAMPLE


#PREREQUISITS
The code is written in Python3 but can be easily adjusted to Python2.7

#REQUIRED PYTHON PACKAGES
numpy
matplotlib
pandas
urllib


#MANUAL ADJUSTMENTS TO BE MADE WHEN USING THIS CODE
## Mandatory
1. chose month you want to plot (line 18)
2. chose local file path to store raw data as txt-file (line 20)
3. chose federal states you want to plot (line 71) by adding the number of the state according to dictionary (lines 61-66)

## Not mandatory adjustments, just to play around:
1. adjust colorbar by changing colors in function custom_div_cmap or use a predifined colorbar from matplotlib
2. adjust reference period to see how this changes the anomalies
3. adjust the limits of the colorbar by chosing different standard deviations


#AUTHORS
Scientists for Future Leipzig
