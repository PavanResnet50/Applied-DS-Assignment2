import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def Read_dataframe(file_name):
    """
    Parameters
    ----------
    file_name : Dataset for the code

    Returns
    -------
    dframe : returns the dataset with yeasr as columns
    dframe2 : returns the dataset with countries as columns

    """
    
    
    dframe = pd.read_csv(file_name, skiprows=3)
    dframe2 = dframe.drop(columns=["Country Code", "Indicator Name", "Indicator Code"], axis=1)
    dframe2 = dframe2.set_index('Country Name')
    dframe2 = dframe2.transpose()
    dframe2 = dframe2.apply(lambda x: pd.to_numeric(x, errors='coerce')) # convert all non-numeric values to NaN

    return dframe, dframe2

file_name = "API_19_DS2_en_csv_v2_4902199.csv"
data_years, data_countries = Read_dataframe(file_name)


def corelation_line(data, indicator):
    """
    

    Parameters
    ----------
    data : Dataset for the code
    indicator : indicator for the graph

    Returns
    -------
    None.

    """
    

    data1 = data.drop(["Country Code","Indicator Code"],axis =1)
    data1.set_index("Indicator Name",inplace = True)
    data1 = data1.loc[indicator]
    data1 = data1.reset_index(level = "Indicator Name")
    data1.groupby(["Country Name"]).sum()
    data1 = data1.loc[data1["Country Name"].isin(["China", "India", "Canada", "Germany","Croatia"]), :]
    
    data1.plot(x= "Country Name",y = ['1980', '1985', '1990','1995','2000','2005',"2010", "2015", "2019"],figsize = (15,5))
    plt.title(indicator)
    plt.show()

corelation_line(data_years, "Urban population growth (annual %)")
corelation_line(data_years, "Total greenhouse gas emissions (kt of CO2 equivalent)")

def corelation_bar(data, indicator):
    """

    Parameters
    ----------
    data : dataset for the code
    indicator : indicator for the code

    Returns
    -------
    None.

    """
    
    
    data1 = data.drop(["Country Code","Indicator Code"],axis =1)
    data1.set_index("Indicator Name",inplace = True)
    data1 = data1.loc[indicator]
    data1 = data1.reset_index(level = "Indicator Name")
    data1.groupby(["Country Name"]).sum()
    data1 = data1.loc[data1["Country Name"].isin(["China", "India", "Canada", "Germany","Croatia"]), :]
    data1.plot(x= "Country Name",y = ['1990','1995','2000','2005', "2010", "2015", "2019"], figsize = (15,5), kind = "bar")
    plt.title(indicator)
    plt.show()

corelation_bar(data_years, "Foreign direct investment, net inflows (% of GDP)")

print(data_countries)


# Group data by country name
grouped_data = data_years.groupby("Country Name")

# Get data for China
china_data = grouped_data.get_group("China")

# Set 'Indicator Name' column as index
china_data = china_data.set_index("Indicator Name")

# Select data for years 2000-2021
china_data = china_data.loc[:, '2000':'2021']

# Transpose the data
china_data = china_data.transpose()

# Select a subset of indicators for analysis
selected_indicators = ["Mortality rate, under-5 (per 1,000 live births)",
                       "Population growth (annual %)",
                       "Urban population growth (annual %)",
                       "Foreign direct investment, net inflows (% of GDP)"]

china_data_subset = china_data[selected_indicators]

# Calculate correlation matrix
corr_matrix = china_data_subset.corr()

# Rename rows and columns of correlation matrix
corr_matrix.index = ["Mortality rate", "Population growth", "Urban population", "Foreign investments"]
corr_matrix.columns = ["Mortality rate", "Population growth", "Urban population", "Foreign investments"]

# Plot heatmap of correlation matrix
sns.heatmap(corr_matrix, annot=True, cmap="RdBu")
plt.title("Correlation between selected indicators in China") 

    
    
    
'''
data1= data_years
data1 = data_years.drop(["Country Code","Indicator Code"],axis =1)
data1.set_index("Indicator Name",inplace = True)
data1 = data1.loc["Forest area (% of land area)"]
data1 = data1.reset_index(level = "Indicator Name")
data1.groupby(["Country Name"]).sum()
#data1 = data1.head(10)
data1 = data1.loc[data1["Country Name"].isin(["India", "Afghanistan", "Bangladesh", "Canada", "United Kingdom", "Brazil", "Germany", "Australia", "Croatia","China"]), :]

data1.plot(x= "Country Name",y = ['1965', '1970', '1975', '1980', '1985', '1990','1995','2000','2005',],figsize = (15,5))
plt.title("Forest area (% of land area)")
plt.show()

data2 = data_years
data2 = data_years.drop(["Country Code","Indicator Code"],axis =1)
data2.set_index("Indicator Name",inplace = True)
data2 = data2.loc["Total greenhouse gas emissions (kt of CO2 equivalent)"]
data2 = data2.reset_index(level = "Indicator Name")
data2.groupby(["Country Name"]).sum()
data2 = data2.loc[data2["Country Name"].isin(["India", "Afghanistan", "Bangladesh", "Canada", "United Kingdom", "Brazil", "Germany", "Australia", "Croatia","China"]), :]
#data2 = data2.head(10)
data2.plot(x= "Country Name",y = ['1965', '1970', '1975', '1980', '1985', '1990','1995','2000','2005',],figsize = (15,5))
plt.title("Total greenhouse gas emissions (kt of CO2 equivalent)")
plt.show()
'''