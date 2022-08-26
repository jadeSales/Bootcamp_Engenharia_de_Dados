#%%
from ctypes.wintypes import WCHAR
from signal import valid_signals
from sunau import Au_read
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# %%
url = 'https://www.vivareal.com.br/venda/sp/sao-paulo/apartamento_residencial/?pagina={}'

# %%
i = 1
ret = requests.get(url.format(i))
soup = bs(ret.text)

# %%
soup
# %%
houses = soup.find_all(
    'a', {'class': 'property-card__content-link js-card-title'}
)

qtd_imoveis = float(soup.find('strong', {'class': 'results-summary__count js-total-records'}).text.replace('.', ''))

# %%
houses
# %%
len(houses)
# %%
qtd_imoveis
# %%
house = houses[0]
# %%
house
# %%
df = pd.DataFrame(
    columns = [
        'descricao',
        'endereco',
        'area',
        'quartos',
        'banheiros',
        'vagas',
        'valor',
        'condominio',
        'wlink',
    ]
)
i = 0
#%%
while qtd_imoveis > df.shape[0]:
    i += 1
    print(f"valor i: {i} \t\t qtd_imoveis: {df.shape[0]}")
    ret = requests.get(url.format(i))
    soup = bs(ret.text)
    houses = soup.find_all(
        'a', {'class': 'property-card__content-link js-card-title'})
    for house in houses:
        try:
            descricao = house.find('span', {'class': 'property-card__title js-cardLink js-card-title'}).text.strip()
        except:
            descricao = None
        try:
            endereco = house.find('span', {'class': 'property-card__address'}).text.strip()
        except:
            endereco = None
        try:
            area = house.find('span', {'class': 'js-property-card-detail-area'}).text.strip()
        except:
            area = None
        try:
            quartos = house.find('li', {'class': 'property-card__detail-room'}).span.text.strip()
        except:
            quartos = None
        try:
            banheiros = house.find('li', {'class': 'property-card__detail-bathroom'}).span.text.strip()
        except: 
            banheiros = None
        try:
            vagas = house.find('li', {'class': 'property-card__detail-garage'}).span.text.strip()
        except: 
            vagas = None
        try:
            valor = house.find('div', {'class': 'property-card__price'}).p.text.strip()
        except:
            valor = None
        try:
            condominio = house.find('strong', {'class': 'js-condo-price'}).text.strip()
        except:
            condominio = None
        try:
            wlink = 'https://www.vivareal.com.br' + house['href']
        except:
            wlink = None

        df.loc[df.shape[0]] = [
            descricao,
            endereco,
            area,
            quartos,
            banheiros,
            vagas,
            valor,
            condominio,
            wlink
        ]

#%%
df

# %%

df.to_csv('banco_de_imoveis.csv', sep=';', index=False)
# %%
