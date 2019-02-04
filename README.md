# Who should use this resource?
Anybody who:
- needs interoperability between country-level datasets from multiple sources.
- wants the latest official list of countries in a particular international club (e.g, the UN, EU, etc.).

# What problem does this solve?
## IsoToXX files
Different datasets inevitably use different country names and codes. Converting all country names and codes to ISO codes at the beginning of every cross-country project makes it possible to quickly use and compare data across, e.g., a UN database that has data for the **Democratic Republic of the Congo**, a World Bank database with information about **Congo, Dem. Rep.** and an Oxford Economics database that has data for **Congo, DR**.

Tip: Only convert the ISO codes back to country names, in the style and language of your chice, once your analysis is complete and it's time to start creating charts and tables for your report or presentation.

## CountryList files
Saves you the 60 seconds it takes to find the official website of the country club in question and remove whatever website formatting that makes it tedious to quickly incorporate the country names into your spreadsheet.

# What is in this repository?
This repository contains:
- conversion files (called IsoToXX) which allow you to standardise your datasets so that they use ISO codes.
- up-to-date lists of member countries in various clubs (e.g., the EU, OECD, ASEAN, etc.).
- Python program files that you can use automatically fetch updated country lists from official websites.

# Possible future additions
- Mercosur
- APEC
