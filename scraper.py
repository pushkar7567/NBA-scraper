import requests
import html5lib
import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate

stats = input("Player or YearPool P/Y: ")
if (stats == "P"):
    player_name = input("Enter Player Full Name: ")
    pname_str = player_name.lower()
    lname_ind = pname_str.find(" ")
    fpname_str = pname_str[lname_ind+1]+"/"+pname_str[lname_ind+1:lname_ind+6]
    fpname_str = fpname_str + pname_str[0:2]
    fpname_str = fpname_str + "01"
    URL = "https://www.basketball-reference.com/players/{}.html".format(fpname_str)

    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')

    career_stats = soup.find('table', attrs = {'id':'per_game'})
    career_table = pd.read_html(str(career_stats))
    career_table = career_table[0]
    print(career_table)

elif  (stats == "Y"):
    year = input("Enter Year:")
    if (int(year)>2016):
        URL = "https://www.basketball-reference.com/leagues/NBA_{}.html".format(year)

        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'lxml')

        tableE = soup.find('table', attrs = {'id':'confs_standings_E'})
        e_standing_table = pd.read_html(str(tableE))

        tableW = soup.find('table', attrs = {'id':'confs_standings_W'})
        w_standing_table = pd.read_html(str(tableW))

        print(tabulate(e_standing_table[0], headers=['->', 'Eastern Conference', 'W', 'L', 'W/L%', 'GB','PS/G', 'PA/G', 'SRS'], tablefmt='psql'))
        print(tabulate(w_standing_table[0], headers=['->', 'Western Conference', 'W', 'L', 'W/L%', 'GB','PS/G', 'PA/G', 'SRS'], tablefmt='psql'))

    else:
        URL = "https://www.basketball-reference.com/leagues/NBA_{}_standings.html".format(year) 

        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'lxml')

        tableE = soup.find('table', attrs = {'id':'divs_standings_E'})
        e_standing_table = pd.read_html(str(tableE))

        tableW = soup.find('table', attrs = {'id':'divs_standings_W'})
        w_standing_table = pd.read_html(str(tableW))

        print(e_standing_table)
        print(w_standing_table)