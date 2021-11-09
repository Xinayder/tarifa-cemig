import requests
from bs4 import BeautifulSoup

URL_TARIFAS = "https://www.cemig.com.br/atendimento/valores-de-tarifas-e-servicos/"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"

headers = {
    'User-Agent': USER_AGENT
}

tarifas = {
    'B1': {
        'normal': {},
        'baixa_renda': {},
        'branca': {},
    },
    'B2': {
        'normal': {},
        'jequitinhonha': {},
        'demais_regioes': {},
        'branca': {},
    },
    'B3': {
        'normal': {},
        'branca': {},
    },
    'B4': {
        'B4a': {},
        'B4b': {},
    }
}

page = requests.get(URL_TARIFAS, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("section", class_="table")

def get_tarifa_b1_normal(tbl):
    tbody = tbl.find("tbody")
    valores = tbody.find_all("td")

    print('Obtendo tarifas B1 Residencial Normal...')
    
    tarifas['B1']['normal'] = {
        'verde': float(valores[1].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'amarela': float(valores[2].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_1': float(valores[3].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_2': float(valores[4].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'escassez': float(valores[5].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
    }

def get_tarifa_b1_res_br(tbl):
    tbody = tbl.find("tbody")
    valores = tbody.find_all("td")

    print('Obtendo tarifas B1 Residencial Baixa Renda...')

    tarifas['B1']['baixa_renda'] = {
        'lt_30': {
            'verde': float(valores[1].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
            'amarela': float(valores[2].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
            'vermelha_1': float(valores[3].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
            'vermelha_2': float(valores[4].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
            'escassez': float(valores[5].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        },
        '31-100': {
            'verde': float(valores[7].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
            'amarela': float(valores[8].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
            'vermelha_1': float(valores[9].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
            'vermelha_2': float(valores[10].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
            'escassez': float(valores[11].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        },
        '101-220': {
            'verde': float(valores[13].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
            'amarela': float(valores[14].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
            'vermelha_1': float(valores[15].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
            'vermelha_2': float(valores[16].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
            'escassez': float(valores[17].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        },
        'gt-220': {
            'verde': float(valores[19].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
            'amarela': float(valores[20].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
            'vermelha_1': float(valores[21].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
            'vermelha_2': float(valores[22].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
            'escassez': float(valores[23].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        }
    }

def get_tarifa_b2_rur(tbl):
    tbody = tbl.find("tbody")
    valores = tbody.find_all("td")

    print('Obtendo tarifas B2 Rural...')
    
    tarifas['B2']['normal'] = {
        'verde': float(valores[1].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'amarela': float(valores[2].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_1': float(valores[3].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_2': float(valores[4].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'escassez': float(valores[5].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
    }
    
    tarifas['B2']['jequitinhonha'] = {
        'verde': float(valores[7].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'amarela': float(valores[8].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_1': float(valores[9].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_2': float(valores[10].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'escassez': float(valores[11].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
    },

    tarifas['B2']['demais_regioes'] = {
        'verde': float(valores[13].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'amarela': float(valores[14].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_1': float(valores[15].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_2': float(valores[16].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'escassez': float(valores[17].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
    },

def get_tarifa_b3(tbl):
    tbody = tbl.find("tbody")
    valores = tbody.find_all("td")

    print('Obtendo tarifas B3 Demais Classes...')
    
    tarifas['B3']['normal'] = {
        'verde': float(valores[1].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'amarela': float(valores[2].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_1': float(valores[3].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_2': float(valores[4].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'escassez': float(valores[5].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
    }

def get_tarifa_b4(tbl):
    tbody = tbl.find("tbody")
    valores = tbody.find_all("td")

    print('Obtendo tarifas B4 Iluminacao Publica...')
    
    tarifas['B4']['B4a'] = {
        'verde': float(valores[1].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'amarela': float(valores[2].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_1': float(valores[3].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_2': float(valores[4].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'escassez': float(valores[5].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
    }

    tarifas['B4']['B4b'] = {
        'verde': float(valores[7].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'amarela': float(valores[8].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_1': float(valores[9].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_2': float(valores[10].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'escassez': float(valores[11].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
    }

def get_tarifa_branca(tbl):
    tbody = tbl.find("tbody")
    valores = tbody.find_all("td")

    print('Obtendo tarifas Tarifa Branca...')

    offset = 0
    tarifas['B1']['branca']['ponta'] = {
        'verde': float(valores[1 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'amarela': float(valores[2 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_1': float(valores[3 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_2': float(valores[4 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'escassez': float(valores[5 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
    }

    offset = 6
    tarifas['B1']['branca']['intermediario'] = {
        'verde': float(valores[1 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'amarela': float(valores[2 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_1': float(valores[3 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_2': float(valores[4 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'escassez': float(valores[5 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
    }

    offset = 12
    tarifas['B1']['branca']['fora_ponta'] = {
        'verde': float(valores[1 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'amarela': float(valores[2 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_1': float(valores[3 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_2': float(valores[4 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'escassez': float(valores[5 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
    }

    offset = 18
    tarifas['B2']['branca']['ponta'] = {
        'verde': float(valores[1 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'amarela': float(valores[2 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_1': float(valores[3 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_2': float(valores[4 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'escassez': float(valores[5 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
    }

    offset = 24
    tarifas['B2']['branca']['intermediario'] = {
        'verde': float(valores[1 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'amarela': float(valores[2 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_1': float(valores[3 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_2': float(valores[4 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'escassez': float(valores[5 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
    }

    offset = 30
    tarifas['B2']['branca']['fora_ponta'] = {
        'verde': float(valores[1 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'amarela': float(valores[2 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_1': float(valores[3 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_2': float(valores[4 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'escassez': float(valores[5 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
    }

    offset = 36
    tarifas['B3']['branca']['ponta'] = {
        'verde': float(valores[1 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'amarela': float(valores[2 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_1': float(valores[3 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_2': float(valores[4 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'escassez': float(valores[5 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
    }

    offset = 42
    tarifas['B3']['branca']['intermediario'] = {
        'verde': float(valores[1 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'amarela': float(valores[2 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_1': float(valores[3 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_2': float(valores[4 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'escassez': float(valores[5 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
    }

    offset = 48
    tarifas['B3']['branca']['fora_ponta'] = {
        'verde': float(valores[1 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'amarela': float(valores[2 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_1': float(valores[3 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'vermelha_2': float(valores[4 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
        'escassez': float(valores[5 + offset].text.strip().replace(',', '.').encode('ascii', 'ignore').decode()),
    }

def get_tarifas():
    get_tarifa_b1_normal(results[0])
    get_tarifa_b1_res_br(results[1])
    get_tarifa_b2_rur(results[2])
    get_tarifa_b3(results[3])
    get_tarifa_b4(results[4])
    get_tarifa_branca(results[5])

get_tarifas()

import json
with open('tariffs.json', 'w', encoding='utf-8') as f:
    json.dump(tarifas, f, ensure_ascii=False, indent=4)