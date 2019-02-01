# Get UN country list

# Install dependencies
# pip install requests
# pip install BeautifulSoup4

import urllib.request
from bs4 import BeautifulSoup
import datetime
import datetime

page = urllib.request.urlopen('https://europa.eu/european-union/about-eu/countries_en')

soup = BeautifulSoup(page,'html.parser')



soup = soup.find('div',id="year-entry2")

soup = soup.find_all('a')

# Initialise new csv file
f=open('../CountryList-EU.csv','w')
f.write('EuMemberStates'+datetime.datetime.today().strftime('%Y-%m-%d')+'\n')
f.close()

# Add countries
for x in soup:
	soup = x.text
	print(soup)
	f=open('../CountryList-EU.csv','a')
	f.write(soup+'\n')
	f.close()
	
