# vpap_lens
A tool to pipe out varying political donation data from vpap dot org

## Summary
The goal was to start off by targeting different zip codes and return a list of donor information from vpap.

There are varying use cases for such data - It's unfortunate that the data cannot be accessed via API or data dump (if you do find it please let us know!).

## How to use
At the top of the file there is a list of zip codes. Plug in your zip code list there i.e. [22201, 22202, 22203].<br>
Running the program will loop through those zip codes and return the donor data for those locations.

The final overall output will be saved to: final_output_csv.txt

This can be opened in excel and other workbook programs.
When opening, the data is TAB delimited.

Output to the terminal while running will print the URL used, the growing dataset, and dataframe outputs from Pandas.

## Requirements (pip installs)
- requests
- lxml
- pandas

## TODO
Feel free to contribute / optimize / modify. Below are some things that need to be done:
 - Clean output (whitespace and newlines (\n)) (DONE)
 - Maybe build out some graphing tools
 - Whatever else you may come up with :)

## Terms of Service:
 - According to vpap dot org you cannot use their data for commercial use
 - Review vpap dot org terms of service prior to use
 - Read the code before running and understand what it's doing
 - Follow all applicable internet laws and vpap TOS
 - Do NOT spam vpap dot org, keep scraping intervals at a respectful delay
 - license for vpap_lens is GPLv3 but that does not include vpap dot org site/data
 - We are not responsible the use nor data validity of this tool - use at your own risk

## Attribution
Thanks to https://www.vpap.org/

## vpap dot org Terms of Service:
https://www.vpap.org/about-us/terms-of-service/
