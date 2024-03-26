
# test Api pokmonbatle

import requests 

URL = 'https://api.pokemonbattle.me/v2'
HEADER = {'Content-Type' : 'application/json',
           'trainer_token' : 'da102757308f05c7b70f9364c35ebe8d'}                                               
TOKEN = 'da102757308f05c7b70f9364c35ebe8d'


  
body = {
    
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

# создание покемона

response = requests.post(url= f'{URL}/pokemons', headers = HEADER, json = body, timeout=10)
print(f'статус код: {response.status_code}.Сообщение:{response.json()['message']}')
response_json = response.json()
key_id_pokemon = response_json["id"]
"""body3 = {
"pokemon_id": "id"
}
#убить покемона 
response = requests.post(url=f'{URL}/pokemons/khockout', json=body3, headers=HEADER, timeout=10)
"""

body2 = {
    "pokemon_id" : key_id_pokemon,
    "name" : "новый бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"

}

# изменение имени покемона
response = requests.put(url=f'{URL}/pokemons', json=body2, headers=HEADER, timeout=10)
print(f'статус код: {response.status_code}.Сообщение:{response.json()['message']}')

body4 = {
    "pokemon_id": key_id_pokemon
}
#поймать покемона в покебол
response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body4, headers=HEADER, timeout=10)
print(f'статус код: {response.status_code}.Сообщение:{response.json()['message']}')







