#%%
#REQUISIÇÃO PÚBLICA PARA PEGAR A QUITAÇÃO DO DÓLAR NOS ÚLTIMOS 30 SEGUNDOS
#imports - inportando bibliotecas 
import requests 
import json
#%%
url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
ret = requests.get(url) 

#requests
#get quando quer somente pegar os dados
#post quando quer passar informação
#put quando quer alterar algum dado 

# %%
if ret:
    print(ret)
else:
    print('Xii Falhou, informação não existe')
# %%
print(ret.text)
# %%
#tratando documento jsonc(dicionário)
dolar = json.loads(ret.text)['USDBRL'] #pegando só a segunda chave

# %%
#acessa a o valor da chave bid, que está como text
dolar['bid']
# %%
#converter de texto para float e multiplicando por 20
print(f" 20 dólares hoje custam {float(dolar['bid'])*20} reais")
# %%

# CRIANDO FUNÇÃO DO COD ANTERIOR

def cotacao(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-', '')] #substituindo hífen por nada
    print(
        f" {valor} {moeda[:3]} hoje custam {float(dolar['bid'])*valor} {moeda[-3:]}")
# %%
#chamando função
cotacao(20, 'USD-BRL')
# %%
cotacao(20, 'JPY-BRL')
# %%
## TRATANDO ERROS E RETENTATIVAS 

lst_money = [
    "USD-BRL",
    "EUR-BRL",
    "BTC-BRL",
    "JPY-BRL",
    "RPL-BRL"
]

valor = 20

for moeda in lst_money:
    try:
        url = f'https://economia.awesomeapi.com.br/last/{moeda}'
        ret = requests.get(url)
        dolar = json.loads(ret.text)[moeda.replace('-', '')] #substituindo hífen por nada
        print(
            f" {valor} {moeda[:3]} hoje custam {float(dolar['bid'])*valor} {moeda[-3:]}")
    except:
        print(f"Falha na moeda: {moeda}")
# %%

## TRATANDO ERROS COM DECORADOR
#decorador é aplicado antes das soluções

#criando uma função onde o parâmetro é outra função, e dentro da função é uma subfunção
def error_check(func): 
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except:
            print(f"{func.__name__} falhou")
    return inner_func
# %%
# TRATANDO ERROS COM DECORADOR
# Utilizando a biblioteca backoff

import backoff
import random

@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionAbortedError, TimeoutError), max_tries=10)
def test_func(*args, **kargs):
    rnd = random.random()
    log.debug(f" RND: {rnd}")
    log.info(f" args: {args if args else 'sem args'}")
    log.info(f" kargs: {kargs if kargs else 'sem kargs'}")
    if rnd < .2:
        log.error('Conexão foi finalizada')
        raise ConnectionAbortedError('Conexão foi finalizada')
    elif rnd < .4:
        log.error('Conexão foi recusada')
        raise ConnectionRefusedError('Conexão foi recusada')
    elif rnd < .6:
        log.error('Tempo de espera excedido')
        raise TimeoutError('Tempo de espera excedido')
    else:
        return "OK!"
# %%
test_func()

# %%
# LOGS - informações de saídas
import logging

# %%
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    #'%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)
# %%
test_func()
# %%

