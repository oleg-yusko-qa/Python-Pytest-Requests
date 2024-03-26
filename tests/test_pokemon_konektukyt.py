import requests
import pytest 

URL = 'https://api.pokemonbattle.me/v2'
HEADER = {'Content-Type' : 'application/json'}                                               
TOKEN = 'da102757308f05c7b70f9364c35ebe8d'

def test_status():  #обьявляем функцию тест def
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id": 173})
    assert response.status_code == 200   #assert(утверждаю) переменная response содержит статус код 200 == двойное равно сравнение

def test_part_of_respons():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id": 173})
    assert response.json()['data'][0]['trainer_name'] == 'шаман' # находим имя из 0 массива

