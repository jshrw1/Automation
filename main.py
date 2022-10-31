# Packages
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas

# Obtain data URLs (needed as ONS urls are not always consistent) before cleaning.

url = ['https://www.ons.gov.uk/economy/grossdomesticproductgdp/datasets/gdpmonthlyestimateuktimeseriesdataset',
       'https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/datasets/averageweeklyearnings',
       'https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/datasets/employmentbyindustryemp13']

urls = []
for x in range(len(url)):
    reqs = requests.get(url[x])
    soup = BeautifulSoup(reqs.text, 'html.parser')
    for link in soup.find_all('a'):
        urls.append(link.get('href'))

match = [s for s in urls if ".xls" in s]

# Download and save xls/xlsx files

path = "C:/Users/Joshua Rawlings/Documents/PyCharmProjects/automation_risk"

for x in match:
    file = requests.get('https://www.ons.gov.uk' + x, verify=True)
    ext = (x.split("/")[-1:])
    open(path + '/' + ext[0], 'wb').write(file.content)
