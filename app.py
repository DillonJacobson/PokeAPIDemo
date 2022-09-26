
from random import randint
import requests
from flask import Flask

app = Flask(__name__)

POKE_API_BASE_URL = 'https://pokeapi.co/api/v2'

@app.route('/api/pokedex', methods=['GET'])
def list_pokemon():
    pokemon_list = [
        "charizard",
        "torterra",
        "gyarados",
        "garchomp",
        "rayquaza"
    ]

    pokemon_result = []
    happiness = []
    
    for pokemon in pokemon_list:
        request_url = f'{POKE_API_BASE_URL}/pokemon/{pokemon}'
        
        # Get base data and ensure pokemon exists
        base_request = requests.get(request_url)
        if base_request.status_code != 200:
            return {
                'message': 'An error has occured',
                'error': base_request.text,
                'pokemon': pokemon
            }, base_request.status_code
        base_data = base_request.json()

        # Get species data
        species_request = requests.get(base_data['species']['url'])
        if species_request.status_code != 200:
            return {
                'message': 'An error has occured',
                'error': species_request.text,
                'pokemon': pokemon
            }, species_request.status_code
        species_data = species_request.json()
        
        # Pick 2 random moves
        moves = []
        for i in range(2):
            moveIdx = randint(0, len(base_data['moves'])-1)
            if base_data['moves'][moveIdx] not in moves:
                moves.append(base_data['moves'][moveIdx]['move']['name'])
        
        # Build result entry
        pokemon_result.append(
            {
                'id': base_data['id'],
                'url': request_url,
                'name': base_data['name'],
                'height': base_data['height'],
                'weight': base_data['weight'],
                'moves': moves,
                'color': species_data['color']['name'],
                'base_happiness': species_data['base_happiness']
            }
        )
        # Add entry for happiness calculations
        happiness.append(species_data['base_happiness'])

    return {
        'pokemon' : pokemon_result,
        'group_happiness': {
            'mean': sum(happiness)/len(happiness),
            'median': sorted(happiness)[len(happiness) // 2],
            'mode': max(happiness, key=happiness.count)
        }
    }, 200