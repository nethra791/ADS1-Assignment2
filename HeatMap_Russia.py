import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew, kurtosis


def plot_heatmap(file_path, ind):
    
    """
    Generate a correlation heatmap and display
    statistical results for given indicators.

    Parameters:
    - file_path (str): Path to the CSV file containing the data.
    - ind (list): List of indicators for correlation analysis.

    Returns:
    - None
    """
    
    # Read data from CSV file into a DataFrame
    data = pd.read_csv(file_path)

    # Extract relevant columns for correlation analysis
    ind_data = data[ind]

    # Calculate correlation matrix
    cor_mat = ind_data.corr()

    # Statistical Analysis using NumPy and SciPy
    # Calculate mean and standard deviation for each indicator
    mean_ind = np.mean(ind_data[ind], axis=0)
    std_ind = np.std(ind_data[ind], axis=0)

    # Calculate skewness and kurtosis for indicators using SciPy's functions
    skew_ind = skew(ind_data[ind], axis=0)
    kur_ind = kurtosis(ind_data[ind], axis=0)

    # Print the statistical results for each indicator
    for i in range(len(ind)):
        print(f"Mean of {ind[i]}: {mean_ind[i]}")
        print(f"Standard Deviation of {ind[i]}: {std_ind[i]}")
        print(f"Skewness of {ind[i]}: {skew_ind[i]}")
        print(f"Kurtosis of {ind[i]}: {kur_ind[i]}")

    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(cor_mat, annot=True, cmap='coolwarm',
            fmt=".2f", linewidths=.5)
    plt.title('Correlation Heatmap for Russia')
    plt.show()


file_path = 'RussiaData.csv'

# Specifying the indicators
sel_ind = ['Health Expenditure', 'Education Expenditure', 
'GDP Growth', 'CO2 Emissions', 'Unemployment Rate', 'Internate Usage']

# Call the function to generate the heatmap and display statistical results
plot_heatmap(file_path, sel_ind)
