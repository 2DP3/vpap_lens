import requests
from lxml import html

# build zip code list (to loop through and build URL dynamically):
zips = [22201, 22202]  # TODO we need to get all of the zip codes here

start_year = "2018"   # TODO make this an input to choose years
end_year = "2019"

url_list = []
results = []

for zip in zips:
    
    # build the URL (with xip and dates modified:
    url = "https://www.vpap.org/" \
    "zipcodes/zcta/{}/donors/" \
    "?page=all" \
    "&zip=22204" \
    "&start_year={}" \
    "&end_year={}" \
    "&recip_type=all".format(zip, start_year, end_year)
    
    # append url to list of urls (for each zip code):
    url_list.append(url)
    
    # get html from url:
    page = requests.get(url)
    
    # convert content for lxml:
    tree = html.fromstring(page.content)
    
    # grab the xpath of the the donor and price tables:
    prices = tree.xpath('//td[@class="right"]/text()')
    donors = tree.xpath('//tr/td/a/text()')

    final_list = []
    i = 0
    
    # loop through first list and match to second:
    for price in prices:
        final_list.append("{}, {}".format(price, donors[i]))
        i = i + 1


print(final_list)






