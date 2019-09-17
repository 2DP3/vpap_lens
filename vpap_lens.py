import requests
from lxml import html
from time import sleep
from pandas import DataFrame
import random

# https://www.vpap.org/sitemap-donors.xml
# https://www.vpap.org/sitemap-candidates.xml

# enter desired zipcodes into this list to iterate through:
zips = [22201, 22202, 22203]

# enter the start and end year for the term which you'd like to parse:
start_year = "2018"
end_year = "2019"

# instantiating various lists to use throughout:
url_list = [] # track urls parsed
results = [] # unused should remove
final_list = [] # final list of prices / donors
df_price_list = [] # price list for pandas df
df_donor_list = [] # donor list for pandas df
df_zip_list = [] # zipcode list for pandas df

# loop through zip code list:
for zip in zips:
    # set up URL for parsing, replacing variables as appropriate:
    url = "https://www.vpap.org/" \
    "zipcodes/zcta/{}/donors/" \
    "?page=all" \
    "&zip={}" \
    "&start_year={}" \
    "&end_year={}" \
    "&recip_type=all".format(zip, zip, start_year, end_year)
    print(url)
    url_list.append(url) # save URL in list
    page = requests.get(url) # make call to url and save HTML
    tree = html.fromstring(page.content) # lxml call to reformat HTML
    # parse LXML to get prices (using XPATH on site HTML)
    prices = tree.xpath('//td[@class="right"]/text()[normalize-space()]')
    # parse LXML to get donors (using XPATH on site HTML)
    donors = tree.xpath('//tr/td/a/text()[normalize-space()]')

    i = 0 # setting iterator to match price list to donor list
    # loop through prices, and append new df list, and adjacent donor and zip code df list evenly (using i)
    for price in prices:
        price = price.strip()
        donor = donors[i].strip()
        df_price_list.append(price.strip())
        df_donor_list.append(donor.strip())
        df_zip_list.append(zip)
        final_list.append(["{}, {}".format(price, donor, zip)])
        i = i + 1
    
    # grab the last page possible from LXML object (HTML) using XATH from page
    total_pages = tree.xpath('//*/a[@class="page-link page"]/text()')

    # loop through all pages, since you did page 1 already, start on 2 and go to the total_pages amount
    for paged in range(2, int(total_pages[2]) + 1):
        sleep(random.randrange(1, 10)) # sleep for a random interval of 1 to 10 seconds
        
        # build new URL
        url = "https://www.vpap.org/" \
              "zipcodes/zcta/{}/donors/" \
              "?page={}" \
              "&zip={}" \
              "&start_year={}" \
              "&end_year={}" \
              "&recip_type=all".format(zip, paged, zip, start_year, end_year)

        print(url)
        url_list.append(url)
        page = requests.get(url)
        tree = html.fromstring(page.content)
        prices = tree.xpath('//td[@class="right"]/text()[normalize-space()]')
        donors = tree.xpath('//tr/td/a/text()[normalize-space()]')

        i = 0
        for price in prices:
            price = price.strip()
            donor = donors[i].strip()
            df_price_list.append(price)
            df_donor_list.append(donor)
            df_zip_list.append(zip)
            final_list.append(["{}, {}".format(price, donor, zip)])
            i = i + 1

        print(final_list)

# build dataframe from all data accumulated (three columns - labeled)
df = DataFrame({'Donor Name': df_donor_list,
                'Donation Amount': df_price_list,
                'Zip Code': df_zip_list})

print(final_list)
print(df)

# save df to csv format
df.to_csv('final_output_csv.txt', sep='\t', index=False)








