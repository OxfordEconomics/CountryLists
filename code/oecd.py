# Get OECD country list

# Install dependencies
# pip install requests
# pip install BeautifulSoup4

import urllib.request
from bs4 import BeautifulSoup
import datetime

page = urllib.request.urlopen('http://www.oecd.org/about/membersandpartners/list-oecd-member-countries.htm')

soup = BeautifulSoup(page,'html.parser')

soup = soup.find('table',align='center')

soup = soup.find_all('a')

print (soup)

# Initialise new csv file
f=open('../CountryList-OECD.csv','w')
f.write('OecdMembers'+datetime.datetime.today().strftime('%Y-%m-%d')+'\n')
f.close()

# Add countries
for x in soup:
	if x.text != 'More on membership and enlargement':
		soup = x.text.title() #use title() to capitalise the beginning of each part of country names
		print(soup)
		f=open('../CountryList-OECD.csv','a')
		f.write(soup+'\n')
		f.close()
	
