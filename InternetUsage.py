import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kurtosis, skew

def plot_line(path_to_file):
    """
    Generate a line plot representing Internet Usage from 2000 to 2020 for different countries.

    Parameters:
    - path_to_file (str): The path to the CSV file containing the dataset.

    Returns:
    None
    """
    # Load the dataset from the CSV file
    data = pd.read_csv(path_to_file)

    # Getting the data of country codes and years
    # Fetched the country codes from the CSV
    country_codes = data['Country Name']
    # The columns of years start from the 3rd column.
    years = data.columns[1:]

    # Create a line plot with multiple lines based on the number of countries
    plt.figure(figsize=(10, 6))
    for idx in range(len(country_codes)):
        # The data of years starts from column 3.
        plt.plot(years, data.iloc[idx, 1:], label=country_codes[idx])
 
    # Adding plot title and axis labels to append to the graphs.
    plt.title('Internet Usage from 2000 to 2020')
    plt.xlabel('Years')
    plt.ylabel('Individuals using the Internet (% of population)')

    # Adding legend to the map countrywide
    plt.legend()

    # Display the plot after generating
    plt.show()

    # Statistical Analysis using NumPy and SciPy
    # Calculate mean and standard deviation
    mean_yield = np.mean(data.iloc[:, 1:], axis=0)
    std_yield = np.std(data.iloc[:, 1:], axis=0)

    # Calculate skewness and kurtosis using SciPy's skewness and kurtosis functions
    skewness_yield = skew(data.iloc[:, 1:], axis=1)
    kurtosis_yield = kurtosis(data.iloc[:, 1:], axis=1)

    # Print the statistical results
    print("Mean of Internet Usage: ", mean_yield)
    print("Standard Deviation of Internet Usage: ", std_yield)
    print("Skewness of Internet Usage: ", skewness_yield)
    print("Kurtosis of Internet Usage: ", kurtosis_yield)

# Calling the function to generate the Line Plot
path_to_file = 'InternetUsage.csv'
plot_line(path_to_file)
