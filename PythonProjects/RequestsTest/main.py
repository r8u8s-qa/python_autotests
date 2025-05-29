import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6b28c1d5520960d1a25aa7f91268dd69'
HEADER = {'Content-Type':'application/json' , 'trainer_token':TOKEN}

body_create = {
    "name": "pobeda",
    "photo_id": 12
}
body_change = {
    "pokemon_id": "327786",
    "name": "beda",
    "photo_id": 7
}
body_catch = {
    "pokemon_id": "327786"
}


'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print (response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons' , headers = HEADER, json = body_change)
print (response_change.text)'''

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print (response_catch.text)