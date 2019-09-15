# vpap_lens
A tool to pipe out varying political donation data from vpap dot org

## Summary
This is the first project from the 2DP3 meetup group in DC.
The goal was to start off by targeting different zip codes and return a list of the donor amount and their name for Arlington, Virginia.

There are varying use cases for such data - It's unfortunate that the data cannot be accessed via API or data dump (if you do find it please let us know!).

## How to use
At the top of the file there is a list of zip codes. Plug in your zip code list there i.e. [22201, 22202, 22203]. Running the program will loop through those zip codes on vpap dot org and return the donor data for those locations.

Each page will be saved as: zip_{zipcode}_page_{pagenumber}.txt
The final overall output will be saved to: final_output.txt

## Requirements
- requests
- lxml

## Terms of Service:
 - According to vpap dot org you cannot use their data for commercial use
 - Review vpap dot org terms of service prior to use
 - Read the code before running and understand what it's doing
 - Follow all applicable internet laws and vpap TOS
 - Do NOT spam vpap dot org, keep scraping intervals at a respectful delay
 - license for vpap_lens is GPLv3 but that does not include vpap dot org site/data
 - We are not responsible the use of this tool - use at your own risk

## Attribution
Thanks to https://www.vpap.org/

## vpap dot org Terms of Service:
https://www.vpap.org/about-us/terms-of-service/
