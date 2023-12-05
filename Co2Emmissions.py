import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kurtosis, skew

def read_and_process_data(path_to_file):
    """
    Read a dataframe in World-bank format and return two dataframes: 
    one with years as columns and one with countries as columns.

    Parameters:
    - path_to_file (str): The path to the CSV file containing the dataset.

    Returns:
    - df_years (pd.DataFrame): Dataframe with years as columns.
    - df_countries (pd.DataFrame): Dataframe with countries as columns.
    """
    # Load the dataset from the CSV file
    data = pd.read_csv(path_to_file)

    # Extracting the country names and years
    country_names = data['Country Name']
    years = data.columns[2:]

    # Creating a dataframe with years as columns
    df_years = data.copy()
    df_years = df_years.set_index('Country Name')[years].T

    # Creating a dataframe with countries as columns
    df_countries = data.set_index('Country Name') \
                 .drop(columns=['Country Code'], errors='ignore').T

    return df_years, df_countries

def plot_line(df_years):
    """
    Generate a line plot representing CO2 Emissions 
    from 2000 to 2020 for different countries.

    Parameters:
    - df_years (pd.DataFrame): Dataframe with years as columns.

    Returns:
    None
    """
    # Create a line plot with multiple lines based on the number of countries
    plt.figure(figsize=(10, 6))
    for country in df_years.columns:
        plt.plot(df_years.index, df_years[country], label=country)

    # Adding plot title and axis labels to append to the graphs.
    plt.title('CO2 Emissions from 2000 to 2020')
    plt.xlabel('Years')
    plt.ylabel('CO2 emissions (metric tons per capita)')

    # Adding legend to the map countrywide
    plt.legend()

    # Display the plot after generating
    plt.show()

    # Statistical Analysis using NumPy and SciPy
    # Calculate mean and standard deviation
    mean_yield = np.mean(df_years, axis=0)
    std_yield = np.std(df_years, axis=0)

    # Calculate skewness and kurtosis using SciPy
    skewness_yield = skew(df_years, axis=0)
    kurtosis_yield = kurtosis(df_years, axis=0)

    # Print the statistical results
    print("Mean of CO2 Emissions:\n", mean_yield)
    print("\nStandard Deviation of CO2 Emissions:\n", std_yield)
    print("\nSkewness of CO2 Emissions:\n", skewness_yield)
    print("\nKurtosis of CO2 Emissions:\n", kurtosis_yield)

    # Additional summary statistics using Pandas describe
    print("\nSummary Statistics:\n", df_years.describe())

# Calling the function to read and process the data
path_to_file = 'CO2Emissions.csv'
df_years, df_countries = read_and_process_data(path_to_file)

# Calling to generate Line Plot and performing statistical analysis
plot_line(df_years)
