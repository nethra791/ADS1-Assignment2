import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis


def read_file(filename):
    
    """
    Reads a dataframe in World Bank format and returns two dataframes:
    one with years as columns, and another with countries as columns.

    Parameters:
    - filename (str): Path to the CSV file.

    Returns:
    - Tuple[pd.DataFrame, pd.DataFrame]: A tuple of two dataframes.
    """
    df = pd.read_csv(filename, index_col='Country Name')
    df_y = df.transpose()

    # Clean the transposed dataframe
    df_y.index = pd.to_datetime(
        df_y.index).year
    df_y.index.name = 'Year'

    return df, df_y


def plot_unemp(data):
    
    """
    Plot the unemployment rate over the years for different countries.

    Parameters:
    - data (dict): Dictionary containing unemployment rate data for 
      different countries and years.
    """
    countries = list(data.keys())
    years = list(data[countries[0]].keys())

    bar_width = 0.1
    fig, ax = plt.subplots(figsize=(10, 6))

    for i, year in enumerate(years):
        values = [data[country][year] for country in countries]
        ax.bar([x + i * bar_width for x in range(len(countries))], 
               values, width=bar_width, label=year)

    ax.set_xlabel('Countries')
    ax.set_ylabel('Unemployment rate')
    ax.set_title('Unemployment Rate for Different Countries')
    ax.set_xticks([i + (len(years) - 1) * bar_width / 2 
                   for i in range(len(countries))])
    ax.set_xticklabels(countries)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.show()

    # using statistics methods
    val = np.array(
        [data[country][year] for year in years for country in countries]
    )
    print("Statistics:")
    print(pd.DataFrame(val).describe())
    print("\nSkewness:", skew(val))
    print("Kurtosis:", kurtosis(val))

# Calling functions to create plot
filename = 'Unemployment.csv'
df_c, df_y = read_file(filename)

# Converting to dictionary format for plotting function
unemp_data = df_c.to_dict(orient='index')
plot_unemp(unemp_data)
