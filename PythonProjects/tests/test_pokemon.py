import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6b28c1d5520960d1a25aa7f91268dd69'
HEADER = {'Content-Type':'application/json' , 'trainer_token':TOKEN}
TRAINER_ID = '33618'

def tests_status_code():
    response = requests.get(url = f'{URL}/trainers', headers = HEADER) 
    assert response.status_code == 200


def tests_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', headers = HEADER , params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == "33618"
    