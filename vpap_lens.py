import requests
from lxml import html
from time import sleep

# https://www.vpap.org/sitemap-donors.xml
# https://www.vpap.org/sitemap-candidates.xml

zips = [22201]

start_year = "2018"
end_year = "2019"

url_list = []
results = []
final_list = []

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
    prices = tree.xpath('//td[@class="right"]/text()')
    donors = tree.xpath('//tr/td/a/text()')

    i = 0
    for price in prices:
        final_list.append(["{}, {}".format(price, donors[i])])
        i = i + 1

    total_pages = tree.xpath('//*/a[@class="page-link page"]/text()')
    # print(total_pages[2])


    for paged in range(1, int(total_pages[2]) + 1):
        sleep(3)
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
        prices = tree.xpath('//td[@class="right"]/text()')
        donors = tree.xpath('//tr/td/a/text()')

        i = 0
        for price in prices:
            final_list.append(["{}, {}".format(price, donors[i])])
            i = i + 1

        print(final_list)
        with open("zip_{}_page_{}.txt".format(zip, paged), 'a') as file:
            for item in final_list:
                file.write(item[0])

print(final_list)
with open("final_output.txt", 'w') as file:
    for item in final_list:
        file.write(item[0])








