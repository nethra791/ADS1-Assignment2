import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew, kurtosis


def read_file(file_name):
    
    """
    Reads a DataFrame in Worldbank format and returns two DataFrames:
    one with years as columns, another with countries as columns.

    Parameters:
    - file_name (str): Filename of the CSV file to read.

    Returns:
    - Tuple of two DataFrames: (df_y, df_c)
    """
    df = pd.read_csv(file_name, index_col=0)
    df_y = df.T
    df_c = df

    # Cleaning NaNs or placeholders
    df_y = df_y.apply(pd.to_numeric, errors='coerce')
    df_c = df_c.apply(pd.to_numeric, errors='coerce')

    return df_y, df_c


def plot_gdp(data):
    
    """
    Plot the GDP Growth rate over the years for different countries.
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
    ax.set_ylabel('GDP growth (annual %)')
    ax.set_title('GDP growth Over the Years for Different Countries')

    ax.set_xticks([i + (len(years) - 1) * bar_width / 2 
                   for i in range(len(countries))])
    ax.set_xticklabels(countries)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.show()

    val_array = np.array([data[country][year] for year in years 
                             for country in countries])

    print("Statistics:")
    print(pd.DataFrame(val_array).describe())
    print("\nSkewness:", skew(val_array))
    print("Kurtosis:", kurtosis(val_array))


# Calling function to create plot
file_path = 'GDP.csv'
df_y, df_c = read_file(file_path)

gdp_data = df_c.to_dict(orient='index')
plot_gdp(gdp_data)
