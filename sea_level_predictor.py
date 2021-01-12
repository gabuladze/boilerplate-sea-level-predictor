import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('./epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(1, figsize=(16,5), dpi=150)
    plt.scatter(x=data['Year'], y=data['CSIRO Adjusted Sea Level'])
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')

    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()