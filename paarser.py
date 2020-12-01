import requests
from bs4 import BeautifulSoup
base_url = 'https://kinoteatr.ru'
r = requests.get(f'{base_url}/raspisanie-kinoteatrov')
soap = BeautifulSoup(r.text, 'lxml')
print(soap)
cinemas = []
for i in soap.findAll('div', class_='col-md-12 cinema_card'):
    name = i.find('h3').text.strip()
    href = i.find('a')['href'].strip()
    address = i.findAll('span', class_= 'sub_title')[0].text.strip()
    cinemas.append({
        'name': name,
        'href': href,
        'address': address
    })
    print(name, href, address, sep='\n', end='\n---------------------\n')
    
for i, cinema in enumerate(cinemas):
r = requests.get(cinema['href'])
soap = BeautifulSoup(r.text, 'lxml')
films = soap.findAll('div', class_ = 'shedule_movie bordered gtm_movie')
allfilms = []
for film in films:
    films_dict.append({
    'name':film['data-gtm-list-item-filmname'],
    'href': film.find('a', class_ = 'gtm-ec-list-item-movie')['href'],
    'format': film['data-gtm-format'],
    'genre': film['data-gtm-list-item-genre'],
    'raiting_sub': film.findAll('i', class_ = 'raiting_sub')[0].text.strip(),
    'allrasp': film.findAll('span', class_ = 'shedule_session_time')
    })
cinemas[i]['films'] = allfilms

