import requests
from lxml import html
from time import sleep
from pandas import DataFrame
import random

# https://www.vpap.org/sitemap-donors.xml
# https://www.vpap.org/sitemap-candidates.xml

zips = [22201, 22202, 22203]

start_year = "2018"
end_year = "2019"

url_list = []
results = []
final_list = []
df_price_list = []
df_donor_list = []
df_zip_list = []

for zip in zips:
    url = "https://www.vpap.org/" \
    "zipcodes/zcta/{}/donors/" \
    "?page=all" \
    "&zip={}" \
    "&start_year={}" \
    "&end_year={}" \
    "&recip_type=all".format(zip, zip, start_year, end_year)
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
        df_price_list.append(price.strip())
        df_donor_list.append(donor.strip())
        df_zip_list.append(zip)
        final_list.append(["{}, {}".format(price, donor, zip)])
        i = i + 1

    total_pages = tree.xpath('//*/a[@class="page-link page"]/text()')
    # print(total_pages[2])

    for paged in range(2, int(total_pages[2]) + 1):
        sleep(random.randrange(1, 10))
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

        # with open("zip_{}_page_{}.txt".format(zip, paged), 'a') as file:
        #     for item in final_list:
        #        file.write(item[0])

df = DataFrame({'Donor Name': df_donor_list,
                'Donation Amount': df_price_list,
                'Zip Code': df_zip_list})

print(final_list)
print(df)
df.to_csv('final_output_csv.txt', sep='\t', index=False)








