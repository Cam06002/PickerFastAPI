from bs4 import BeautifulSoup
import requests
import pandas as pd


# dictionary to modify URL scraped, and csv names
team_dict = {
             # Green Bay Packers
             'gnb/2018': 'gnb_2018', 'gnb/2019': 'gnb_2019',
             'gnb/2020': 'gnb_2020', 'gnb/2021': 'gnb_2021',

             # San Francisco 49ers
             'sfo/2018': 'sfo_2018', 'sfo/2019': 'sfo_2019',
             'sfo/2020': 'sfo_2020', 'sfo/2021': 'sfo_2021',
             }

for url, name in team_dict.items():

    # Data URL's
    web = f"https://www.pro-football-reference.com/teams/{url}.htm"
    r = requests.get(web)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.find('table', id='games')

    # Get Columns
    headers = ['weekday', 'day', 'Time', 'Box', 'w_l', 'ot', 'rec', 'location', 'opp', 'TeamPoints', 'OppPoints',
               'Firsts', 'TotYdO', 'PassYO', 'RushYO', 'TeamTOs', 'FirstsA', 'TotYdA', 'PassYA', 'RushYA',
               'ForcedTOs', 'OffenseEx', 'DefenseEx', 'SPtEx']

    data = pd.DataFrame(columns=headers)  # dataframe built with empty rows

    # Get row data
    for j in table.find_all('tr')[2:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(data)
        data.loc[length] = row

    # Clean the data
    data.loc[data['location'] == '', 'location'] = 'Home'
    data.loc[data['location'] == '@', 'location'] = 'Away'

    data.drop('weekday', inplace=True, axis=1)
    data.drop('Time', inplace=True, axis=1)
    data.drop('Box', inplace=True, axis=1)
    data.drop('OffenseEx', inplace=True, axis=1)
    data.drop('DefenseEx', inplace=True, axis=1)
    data.drop('SPtEx', inplace=True, axis=1)

    data['Week'] = data.reset_index().index
    data['Week'] = data['Week'] + 1

    data.replace('', 0, inplace=True)

    data.to_csv(f"{name}.csv", index=False)
