import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kurtosis, skew


def read_data(path_to_file):
    """
    Read a dataframe in World Bank format and return two dataframes:
    one with years as columns and one with countries as columns.

    Parameters:
    - path_to_file (str): The path to the CSV file containing the dataset.

    Returns:
    - DataFrame: Dataframe with years as columns
    - DataFrame: Dataframe with countries as columns
    """
    data = pd.read_csv(path_to_file)
    data_c = data.set_index('Country Name')
    data_y = data_c.T
    return data_y, data_c


def plot_line(data_c):
    """
    Generate a line plot representing Internet Usage from 2000 to 2020 for
    different countries.

    Parameters:
    - data_c (DataFrame): Dataframe with countries as columns

    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    for country in data_c.index:
        plt.plot(data_c.columns, 
           data_c.loc[country], label=country)

    plt.title('Internet Usage from 2000 to 2020')
    plt.xlabel('Years')
    plt.ylabel('Individuals using the Internet (% of population)')
    # adding legend
    plt.legend()
    plt.show()

    mean_yield = np.mean(data_c, axis=0)
    std_yield = np.std(data_c, axis=0)
    skewness_yield = skew(data_c, axis=1)
    kurtosis_yield = kurtosis(data_c, axis=1)

    print("Mean of Internet Usage: ", mean_yield)
    print("Standard Deviation of Internet Usage: ", std_yield)
    print("Skewness of Internet Usage: ", skewness_yield)
    print("Kurtosis of Internet Usage: ", kurtosis_yield)


# Calling the function to process the data
path_to_file = 'InternetUsage.csv'
data_y, data_c = read_data(path_to_file)

# Calling the function to generate the Line Plot
plot_line(data_c)
