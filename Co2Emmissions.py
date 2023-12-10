import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kurtosis, skew


def read_file(path_to_file):
    
    """
    Read a dataframe in World-bank format and return two dataframes: 
    one with years as columns and one with countries as columns.

    Parameters:
    - path_to_file (str): The path to the CSV file containing the dataset.

    Returns:
    - df_y(pd.DataFrame): Dataframe with years as columns.
    - df_c(pd.DataFrame): Dataframe with countries as columns.
    """
    # Load the dataset
    data = pd.read_csv(path_to_file)

    # Extracting the country names and years
    years = data.columns[2:]

    # Creating a dataframe with years as columns
    df_y = data.copy()
    df_y = df_y.set_index('Country Name')[years].T

    # Creating a dataframe with countries as columns
    df_c = data.set_index('Country Name') \
                 .drop(columns=['Country Code'], errors='ignore').T

    return df_y, df_c


def plot_line(df_y):
    """
    Generate a line plot representing CO2 Emissions 
    from 2000 to 2020 for different countries.

    Parameters:
    - df_y (pd.DataFrame): Dataframe with years as columns.

    Returns:
    None
    """
    # Create a line plot
    plt.figure(figsize=(10, 6))
    for country in df_y.columns:
        plt.plot(df_y.index, df_y[country], label=country)

    # Adding plot title and axis labels
    plt.title('CO2 Emissions from 2000 to 2020')
    plt.xlabel('Years')
    plt.ylabel('CO2 emissions (metric tons per capita)')

    # Adding legend
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # Display the plot
    plt.show()

    # Statistical Analysis using NumPy and SciPy
    mean_yield = np.mean(df_y, axis=0)
    std_yield = np.std(df_y, axis=0)

    # Calculate skewness and kurtosis using SciPy
    skewness_yield = skew(df_y, axis=0)
    kurtosis_yield = kurtosis(df_y, axis=0)

    # Print the statistical results
    print("Mean of CO2 Emissions:\n", mean_yield)
    print("\nStandard Deviation of CO2 Emissions:\n", std_yield)
    print("\nSkewness of CO2 Emissions:\n", skewness_yield)
    print("\nKurtosis of CO2 Emissions:\n", kurtosis_yield)

    # summary statistics using Pandas describe()
    print("\nSummary Statistics:\n", df_y.describe())
    

# Calling the function to read and process the data
path_to_file = 'CO2Emissions.csv'
df_y, df_c = read_file(path_to_file)

# Calling to generate Line Plot
plot_line(df_y)
