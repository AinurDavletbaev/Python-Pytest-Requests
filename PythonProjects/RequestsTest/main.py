import requests 

URL = 'https://api.pokemonbattle.me'
TOKEN = '2b63d1e740542db2d9a22fa508dd25cf'
HEADERS = {'Content-Type': 'application/json','trainer_token': TOKEN}
id = 2527 

body = {
    "name": 'Бульбазавр',
    "photo": 'https://dolnikov.ru/pokemons/albums/001.png'
}

response = requests.post(url = f'{URL}/v2/pokemons',headers = HEADERS, json = body)

print(response.text)
body_confirm = {
    "pokemon_id": '16520',
    "name": 'Moonbeam',
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
response_confirm = requests.put(url = f'{URL}/v2/pokemons',headers = HEADERS, json = body_confirm )
print(response_confirm.text)


body_one = {
    "pokemon_id": "16526"
}

response_one = requests.post(url = f'{URL}/v2/trainers/add_pokeball',headers = HEADERS, json = body_one)
print(response_one.text)