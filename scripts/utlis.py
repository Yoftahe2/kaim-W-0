import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pandas.plotting import scatter_matrix

def detect_outliers_iqr(data) :
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 -Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = ((data < lower_bound)| (data > upper_bound)).sum()
    return outliers

def plot_time_series(df):
    # Ensure "Timestamp" column is in datetime format
    df['Timestamp'] = pd.t0_datetime(df['Timestamp'])

    # plot GHI, DNI, DHI, and Tamb over time
    plt.figure(figsize=(10,6))
    plt.plot(df['Timestamp'], df['GHI'], label = 'GHI')
    plt.plot(df['Timestamp'], df['DNI'], label = 'DNI')
    plt.plot(df['Timestamp'], df['DHI'], label = 'DHI')
    plt.plot(df['Timestamp'], df['Tamb'], label = 'Tamb')
    plt.xlabel('Timestamp')
    plt.ylabel('Values')
    plt.title('Change of Variables over Time')
    plt.legend(loc = 'upper right')
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt_show()

def plot_correlation_analysis(data_frame) :
    # Limit the data to the first 1000 rows
    limited_data_frame = data_frame.head(1000)

    # Define columns related to solar radiation and temperature
    solar_temp_columns = ['GHI', 'DNI', 'DHI', 'TModA','TModB']
    wind_columns = ['WS','WSgust', 'WD']

    # compute the correlation matrix for solar radiation and temperature
    correlation_matrix = limited_data_frame[solar_temp_columns].corr()

    # plot the heatmap for the correlation matrix
    plt.figure(figsize=(10,6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Heatmap: Solar Radiation and Temperature')
    plt.show()

    # Generate pair plot to visualize relationship between solar radiation and Temperature
    