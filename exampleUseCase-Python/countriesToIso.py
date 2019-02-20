# Import dependencies
import pandas as pd

# Tell Python where to find your csv that contains non standard country names. In this case it is one directory up, hence: "../"
nonStandardCountryNames = pd.read_csv('../countryList-ASEAN.csv',header=0,index_col=0)

# Tell Python where to find the csv that contains isoFromCountryNames.csv
isoFromCountryNames = pd.read_csv('../isoFromCountryNames.csv',header=0,index_col=1)

# Perform the 'lookup' by merging isoFromCountryNames onto nonStandardCountryNames, keeping all nonStandardCountryNames and only matching values from isoFromCountryNames
standardCountryNames = pd.merge(nonStandardCountryNames,isoFromCountryNames['ISO'], how='left',left_index=True,right_index=True)

# Print the result to the console
print(standardCountryNames)

# Print the result to CSV
standardCountryNames.to_csv('standardCountryNames.csv')
