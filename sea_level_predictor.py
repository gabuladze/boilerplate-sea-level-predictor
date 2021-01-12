import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('./epa-sea-level.csv')
    
    # Create scatter plot
    X, Y = df['Year'], df['CSIRO Adjusted Sea Level']
    plt.figure(1, figsize=(16,5), dpi=150)
    plt.scatter(x=X, y=Y)

    # Create first line of best fit
    lin_regress_res = linregress(X, Y)
    x1 = np.arange(X.min(), 2050)
    y1 = lin_regress_res.slope * x1 + lin_regress_res.intercept
    plt.plot(x1, y1)

    # Create second line of best fit


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()