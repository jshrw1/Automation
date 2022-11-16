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

path = "/Users/joshuarawlings/PycharmProjects/Automation/"

for x in match:
    file = requests.get('https://www.ons.gov.uk' + x, verify=True)
    ext = (x.split("/")[-1:])
    open(path + '/' + ext[0], 'wb').write(file.content)

# Try find a solution that doesn't download the files. instead just gets the latest data ready for processing.

# Process employment data
employment = "/Users/joshuarawlings/PycharmProjects/Automation/emp13aug2022.xls"
emp = pandas.read_excel(employment, sheet_name = "People", header=6, index_col=0)
emp = emp.apply(pd.to_numeric, errors='coerce').loc[:, ~emp.columns.str.contains('^Unnamed')].dropna().round(decimals=0)
