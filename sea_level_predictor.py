import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    # test_plot_data_points & test_plot_lines fail without float_precision
    df = pd.read_csv('./epa-sea-level.csv', float_precision='legacy')
    
    # Create scatter plot
    X1, Y1 = df['Year'], df['CSIRO Adjusted Sea Level']
    plt.figure(1, figsize=(16,5), dpi=150)
    plt.scatter(x=X1, y=Y1)

    # Create first line of best fit
    a1, b1, _, _, _ = linregress(X1, Y1)
    x1 = np.arange(X1.min(), 2050)
    y1 = a1 * x1 + b1
    plt.plot(x1, y1)

    # Create second line of best fit
    df1 = df[df['Year'] >= 2000]
    X2, Y2 = df1['Year'], df1['CSIRO Adjusted Sea Level']
    a2, b2, _, _, _ = linregress(X2, Y2)
    x2 = np.arange(2000, 2050)
    y2 = a2 * x2 + b2
    plt.plot(x2, y2)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()