# Импортирую библиотеки
import requests
import pytest

# Переменные
TOKEN = 'trainer_token'
URL = 'https://api.pokemonbattle.ru/v2'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '6881'

# Проверка статуса ответа метода GET /trainers
def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response2 = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response2.json()['data'][0]["trainer_name"] == "scald1nd"