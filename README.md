# What is in this repository?
This repository contains:
- conversion files (called IsoToXX) which allow you to standardise your datasets so that they use ISO codes.
- up-to-date lists of member countries in various clubs (e.g., the EU, OECD, ASEAN, etc.).
- Python program files that you can use to automatically fetch updated country lists from official websites.
- An example use case in Excel
- Examples of Excel, SQL, and Python use cases documented in this readme

# Who should use this resource?
Anybody who:
- needs interoperability between country-level datasets from multiple sources.
- wants the latest official list of countries in a particular international club (e.g, the UN, EU, etc.).

# What problem does this repository solve?
## IsoFromXX files

Different datasets inevitably use different country names and codes. Converting all country names and codes to ISO codes at the beginning of every cross-country project makes it possible to quickly use and compare data across, e.g., a UN database that has data for the **Democratic Republic of the Congo**, a World Bank database with information about **Congo, Dem. Rep.** and an Oxford Economics database that has data for **Congo, DR**.

*Tip:* Use ISO codes throughout the entire analysis stage of your project. Only convert the ISO codes back to country names, in the style and language of your chice, once your analysis is complete and it's time to start creating charts and tables for your report or presentation.

## CountryList files

Saves you the 60 seconds it takes to find the official website of the country club in question and remove whatever website formatting that makes it tedious to quickly incorporate the country names into your spreadsheet.

# Example uses

This repository has a wide range of use cases. Below are example use cases for Excel, SQL, and Python.

## Excel use case

Here is an [example use case in Excel](https://github.com/OxfordEconomics/CountryLists/tree/master/exampleUseCase-Excel).  

Here is the explanation for the example in Excel: Suppose you have a spreadsheet called nonStandardCountryNames with country names in Column A of Sheet1. Place [IsoFromCountryNames.csv](https://github.com/OxfordEconomics/CountryLists/blob/master/IsoFromCountryNames.csv) in the same folder, open it, then type this into Cell 2 of Column B of nonStandardCountryNames.

```
=INDEX(isoFromCountryNames.csv!$A:$A,MATCH(A2,isoFromCountryNames.csv!$B:$B,0))
```

## SQLite use case

Anything starting with `my` in the code below should be changed to your desired name.

First, open a command prompt by typing `Win + cmd`.

Next, type the following into the command prompt (make sure a copy of [sqlite3.exe](https://www.sqlite.org/index.html) is in the working directory)

```
sqlite3
.open myDatabaseName  /* This will create a database if it doesn't already exist  */
.read myScript.sql
```

Example of what `myScript.sql` could contain:

```
/* Tell sqlite we are about to import some comma separated values files  */
.mode csv

/* Import our standard iso list  */
.import "isoFromCountryNames.csv" isoFromCountryNames

/* Replace with any csv with non-standard country names  */
.import "countryList-EU.csv" myTableWithNonstandardCountryNames  

/************************* Match ISO codes to table containing non-standard country names *************************/
/** Create a table in my database called myTableWithStandardCountryNames **/
CREATE TABLE myTableWithStandardCountryNames AS

/** Populate it with all columns (hence ".*") from a table called myTableWithNonstandardCountryNames, plus the ISO column from IsoFromCountryNames and name that column myPreferredColumnName **/
SELECT myTableWithNonstandardCountryNames.*, isoFromCountryNames.ISO AS ISO

/** The starting table is myTableWithNonstandardCountryNames **/
FROM myTableWithNonstandardCountryNames

/** The table I want to get the ISO names from is isoFromCountryNames**/
LEFT OUTER JOIN isoFromCountryNames

/** Match the columns "EuMemberStates2019-02-20" and "EnglishNames", and find the associated ISO code **/
ON upper(myTableWithNonstandardCountryNames."EuMemberStates2019-02-20") == upper(isoFromCountryNames."EnglishNames");
```

## Python use cases

Two Python use cases are suggested below.

### Match ISO codes to country names with Python

You can find this example in the [exampleUseCase-Python folder](https://github.com/OxfordEconomics/CountryLists/tree/master/exampleUseCase-Python).

```
# Import dependencies
import pandas as pd

# Tell Python where to find your csv that contains non standard country names. In this case, the csv is in the same directory as the python script.
nonStandardCountryNames = pd.read_csv('countryList-ASEAN.csv',header=0,index_col=0)

# Tell Python where to find the csv that contains isoFromCountryNames.csv. In this case, the csv is in the same directory as the python script.
isoFromCountryNames = pd.read_csv('isoFromCountryNames.csv',header=0,index_col=1)

# Perform the 'lookup' by merging isoFromCountryNames onto nonStandardCountryNames, keeping all nonStandardCountryNames and only matching values from isoFromCountryNames
standardCountryNames = pd.merge(nonStandardCountryNames,isoFromCountryNames['ISO'], how='left',left_index=True,right_index=True)

# Print the result to the console
print(standardCountryNames)

# Print the result to CSV
standardCountryNames.to_csv('standardCountryNames.csv')

```

### Update countryList-XX.csv files with Python
Use the Python files to update the the CountryList-XX.csv files.

Before doing anything else, install dependencies by typing these one at a time into your command prompt:

```
pip install requests
pip install BeautifulSoup4
```

To run an individual python file, for example *asean.py*, type the following into your command prompt:

```
py asean.py
```

To run all python files at once, download or clone this repository to your PC, then double click the `RunAll.bat` file in the [updateCountryLists folder](https://github.com/OxfordEconomics/CountryLists/tree/master/updateCountryLists) folder. 





# Your contributions are welcome!
If you have a suggestion for an ISO-name pairing or an international country list, please feel free to [submit a feature request](https://github.com/OxfordEconomics/CountryLists/issues "Raise an Issue") or branch this repo and [submit a pull request](https://yangsu.github.io/pull-request-tutorial/ "A Visual Guide to Pull Requests").

# Possible future additions to CountryList files
- To be requested...
