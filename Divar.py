import requests
from bs4 import BeautifulSoup

r = requests.get('https://divar.ir/s/tehran')
soup = BeautifulSoup(r.text, 'html.parser')
vals = soup.find_all('div', attrs = {'class' : 'kt-post-card__body'})

for value in vals:
    if 'توافقی' in value.text:
        print(value.text)