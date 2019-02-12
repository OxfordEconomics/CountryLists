# Who should use this resource?
Anybody who:
- needs interoperability between country-level datasets from multiple sources.
- wants the latest official list of countries in a particular international club (e.g, the UN, EU, etc.).

# What is in this repository?
This repository contains:
- conversion files (called IsoToXX) which allow you to standardise your datasets so that they use ISO codes.
- up-to-date lists of member countries in various clubs (e.g., the EU, OECD, ASEAN, etc.).
- Python program files that you can use to automatically fetch updated country lists from official websites.

# What problem does this repository solve?
## IsoFromXX files

Different datasets inevitably use different country names and codes. Converting all country names and codes to ISO codes at the beginning of every cross-country project makes it possible to quickly use and compare data across, e.g., a UN database that has data for the **Democratic Republic of the Congo**, a World Bank database with information about **Congo, Dem. Rep.** and an Oxford Economics database that has data for **Congo, DR**.

Tip: Only convert the ISO codes back to country names, in the style and language of your chice, once your analysis is complete and it's time to start creating charts and tables for your report or presentation.

## CountryList files

Saves you the 60 seconds it takes to find the official website of the country club in question and remove whatever website formatting that makes it tedious to quickly incorporate the country names into your spreadsheet.

# Your contributions are welcome!
If you have a suggestion for an ISO-name pairing or an international country list, please feel free to [submit a feature request](https://github.com/OxfordEconomics/CountryLists/issues "Raise an Issue") or branch this repo and [submit a pull request](https://yangsu.github.io/pull-request-tutorial/ "A Visual Guide to Pull Requests").

# Possible future additions to CountryList files
- Mercosur
- APEC


# Use examples
## Excel

Here is an [example in Excel](https://github.com/OxfordEconomics/CountryLists/tree/master/example-StandardiseCountries-Excel).  

Here is the explanation for the example in Excel: Suppose you have a spreadsheet called nonStandardCountryNames with country names in Column A of Sheet1. Place [IsoFromCountryNames.csv](https://github.com/OxfordEconomics/CountryLists/blob/master/IsoFromCountryNames.csv) in the same folder, open it, then type this into column B of nonStandardCountryNames.

```
=INDEX(IsoFromCountryNames.csv!$A:$A,MATCH(A2,IsoFromCountryNames.csv!$B:$B,0))
```

## SQL

Anything starting with `my` in the code below should be changed to your desired name.

First, import your tables. For example, if you use SQLite, enter these commands into the SQLite command line:

```
/************************* Import ISO to your SQL database *************************/
.mode csv
.import "c:/myDirectory/IsoFromCountryNames.csv" IsoFromCountryNames
.import "c:/myDirectory/myTableWithNonstandardCountryNames.csv" myTableWithNonstandardCountryNames
```

Next, put this code into a .sql file and run it, either in a command prompt or in your database manager (e.g., [DBeaver](https://dbeaver.io/)):
```
/************************* Join country ISO codes for REPORTER *************************/
/** Create a table in my database called myTableWithStandardCountryNames **/
CREATE TABLE myTableWithStandardCountryNames AS

/** Populate it with all columns (hence ".*") from a table called myTableWithNonstandardCountryNames, plus the ISO column from IsoFromCountryNames and name that column myPreferredColumnName **/
SELECT myTableWithNonstandardCountryNames.*, IsoFromCountryNames.ISO AS myPreferredColumnName

/** The starting table is myTableWithNonstandardCountryNames **/
FROM myTableWithNonstandardCountryNames

/** The table I want to get the ISO names from is IsoFromCountryNames**/
LEFT OUTER JOIN IsoFromCountryNames

/** I want to get the ISO names starting from the columns myColumnNameContainingNonStandardCountryNames and "English short name" **/
ON upper(myTableWithNonstandardCountryNames.myColumnNameContainingNonStandardCountryNames) == upper(IsoFromCountryNames."English short name");
```

## Python

To update the CountryList-XX.csv files, just download or clone this repository to your PC, then double click the *RunAll.bat* file in the *code* folder.