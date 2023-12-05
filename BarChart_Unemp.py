import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew, kurtosis

def plot_unemp(data):
    """
    Plot the unemployment rate over the years for different countries.

    Parameters:
    - data (dict): Dictionary containing unemployment rate 
	data for different countries and years.
    """

    countries = list(data.keys())
    years = list(data[countries[0]].keys())

    bar_width = 0.1  # Adjust this value to make bars thinner or thicker
	
     # Adjust the figure size as needed
    fig, ax = plt.subplots(figsize=(10, 6))  

    for i, year in enumerate(years):
        values = [data[country][year] for country in countries]
        # Offset the bars for each year to avoid overlap
        ax.bar([x + i * bar_width for x in range(len(countries))], 
            values, width=bar_width, label=year)

    ax.set_xlabel('Countries')
    ax.set_ylabel('Unemployment rate')
    ax.set_title('Unemployment Rate for Different Countries')

    # Center the x-ticks under each group of bars
    ax.set_xticks([i + (len(years) - 1) * bar_width / 2 
      for i in range(len(countries))])
    ax.set_xticklabels(countries)

    # Move legend outside the plot area
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.show()

    # Extract values for descriptive statistics
    values_array = np.array([data[country][year] 
      for year in years for country in countries])

    # Descriptive statistics using NumPy
    print("Descriptive Statistics:")
    print(pd.DataFrame(values_array).describe())

    # Skewness and Kurtosis using Scipy
    print("\nSkewness:", skew(values_array))
    print("Kurtosis:", kurtosis(values_array))

# Read data from CSV
file_path = 'Unemployment.csv'
unemp_data = pd.read_csv(file_path, index_col='Country Name') \
                .to_dict(orient='index')

# Plotting the data with a larger figure size and adjusted legend position
plot_unemp(unemp_data)
