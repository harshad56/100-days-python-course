from bs4 import BeautifulSoup
import requests

raw_url = 'https://www.nfl.com/stats/player-stats/category/passing/2021/REG/all/'
testing_url = 'https://www.nfl.com/stats/player-stats/category/passing/2021/REG/all/passingyards/desc'
stat_list = ['passingyards', 'passingattempts',
             'passingcompletions', 'passingtouchdowns', 'passinginterceptions']

urls = [f'{raw_url}{i}/desc' for i in stat_list]

name_content = requests.get(url=testing_url).content
name_soup = BeautifulSoup(name_content, 'html.parser')


def clean_text(raw_text):
    return raw_text.getText().strip()


names = name_soup.find_all(class_='d3-o-player-fullname')

player_info = {}
name_list = []
for i in range(len(names)):
    name = names[i]
    name_list.append(clean_text(name))

stats_dict = {}
for i in range(len(urls)):
    content = requests.get(url=urls[i]).content
    soup = BeautifulSoup(content, 'html.parser')
    selected_data = soup.find_all(class_='selected')
    stats_dict[stat_list[i]] = [int(clean_text(data))
                                for data in selected_data]

for n in range(len(name_list)):
    player_info[name_list[n]] = {}
    for i in range(len(stat_list)):
        player_info[name_list[n]][stat_list[i]] = stats_dict[stat_list[i]][n]


print(stats_dict)
