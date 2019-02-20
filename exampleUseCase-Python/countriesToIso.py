# Import dependencies
import pandas as pd

nonStandardCountryNames = pd.read_csv('../countryList-UN.csv',header=0,index_col=0)

isoFromCountryNames = pd.read_csv('../isoFromCountryNames.csv',header=0,index_col=1)

standardCountryNames = pd.merge(nonStandardCountryNames,isoFromCountryNames['ISO'], how='left',left_index=True,right_index=True)

print(standardCountryNames)

# Print to CSV
standardCountryNames.to_csv('standardCountryNames.csv')
