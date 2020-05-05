import requests
import html5lib
import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate


year = 2019
URL = "https://www.basketball-reference.com/leagues/NBA_{}.html".format(year)

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'lxml')

tableE = soup.find('table', attrs = {'id':'confs_standings_E'})
e_standing_table = pd.read_html(str(tableE))

tableW = soup.find('table', attrs = {'id':'confs_standings_W'})
w_standing_table = pd.read_html(str(tableW))

print(tabulate(e_standing_table[0], headers=['->', 'Eastern Conference', 'W', 'L', 'W/L%', 'GB','PS/G', 'PA/G', 'SRS'], tablefmt='psql'))








