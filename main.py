# Obtain data URLs (needed as ONS urls are not always consistent) before cleaning.

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = ['https://www.ons.gov.uk/economy/grossdomesticproductgdp/datasets/gdpmonthlyestimateuktimeseriesdataset', 'https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/datasets/employmentbyindustryemp13']

urls = []
for x in range(len(url)):
    reqs = requests.get(url[x])
    soup = BeautifulSoup(reqs.text, 'html.parser')
    for link in soup.find_all('a'):
        urls.append(link.get('href'))

match = [s for s in urls if ".xls" in s]

url_gdp = 'https://www.ons.gov.uk' + match[0]
url_emp = 'https://www.ons.gov.uk' + match[1]

print(url_gdp)
print(url_emp)

# Download and save xls/xlsx files
df_gdp = pd.read_excel(url_gdp)
df_emp = pd.read_excel(url_emp)
