# Импортирую библиотеку
import requests

# Переменные
TOKEN = 'trainer_token'
URL = 'https://api.pokemonbattle.ru/v2'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

# Запрос на создание покемона
body_create_pokemon = {
    "name": "generate",
    "photo_id": -1
}

response_1 = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)

print(f'Статус-код: {response_1.status_code}. Сообщение: {response_1.text}')

# Запрос на смену имени
body_change_pokemons_name = {
    "pokemon_id": "134367",
    "name": "DIVA",
    "photo_id" : 5
}

response_2 = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_pokemons_name)
print(f'Статус-код: {response_2.status_code}. Сообщение: {response_2.text}')

# Запрос на поимку покемона в покебол
body_add_to_pokeball = {
    "pokemon_id": "134367"
}

response_1 = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_to_pokeball)

print(f'Статус-код: {response_1.status_code}. Сообщение: {response_1.text}')

