import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew, kurtosis

def plot_heatmap(file_path, indicators):
    """
    Generate a correlation heatmap and display statistical results for given indicators.

    Parameters:
    - file_path (str): Path to the CSV file containing the data.
    - indicators (list): List of indicators for correlation analysis.

    Returns:
    - None
    """
    
    # Read data from CSV file into a DataFrame
    data = pd.read_csv(file_path)

    # Extract relevant columns for correlation analysis
    indicators_data = data[indicators]

    # Calculate correlation matrix
    correlation_matrix = indicators_data.corr()

    # Statistical Analysis using NumPy and SciPy
    # Calculate mean and standard deviation for each indicator
    mean_indicators = np.mean(indicators_data[indicators], axis=0)
    std_indicators = np.std(indicators_data[indicators], axis=0)

    # Calculate skewness and kurtosis for each indicator using SciPy's functions
    skewness_indicators = skew(indicators_data[indicators], axis=0)
    kurtosis_indicators = kurtosis(indicators_data[indicators], axis=0)

    # Print the statistical results for each indicator
    for i in range(len(indicators)):
        print(f"Mean of {indicators[i]}: {mean_indicators[i]}")
        print(f"Standard Deviation of {indicators[i]}: {std_indicators[i]}")
        print(f"Skewness of {indicators[i]}: {skewness_indicators[i]}")
        print(f"Kurtosis of {indicators[i]}: {kurtosis_indicators[i]}")
        print("----------------------")

    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Correlation Heatmap for South Africa')
    plt.show()


file_path = 'SAData.csv'

# Specifying the indicators of interest
selected_indicators = ['Health Expenditure', 'Education Expenditure', 'GDP Growth', 'CO2 Emissions', 'Unemployment Rate', 'Internate Usage']

# Call the function to generate the heatmap and display statistical results
plot_heatmap(file_path, selected_indicators)
