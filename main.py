import requests
import json
import os

# Base URL for the Pokémon API
API_URL = "https://pokeapi.co/api/v2/pokemon/"
# Directory to store the Pokémon data
DATA_DIR = "pokedex"

def get_pokemon_data(pokemon_name):
    """
    Fetches Pokémon data from the PokeAPI.

    Args:
        pokemon_name (str): The name of the Pokémon to search for.

    Returns:
        dict: A dictionary containing the Pokémon data if found,
              otherwise returns None.
    """
    try:
        response = requests.get(f"{API_URL}{pokemon_name.lower()}")
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            print(f"Error: The Pokémon '{pokemon_name}' was not found. ")
        else:
            print(f"An HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred while making the request: {err}")
    return None

def display_pokemon_info(data):
    """
    Displays the key statistics of a Pokémon.

    Args:
        data (dict): The JSON data of the Pokémon.
    """
    print("\n--- Pokémon Data ---")
    print(f"Name: {data['name'].capitalize()}")
    print(f"Image: {data['sprites']['front_default']}")
    print("-" * 20)
    print("Stats:")
    print(f"  - Weight: {data['weight']} lbs")
    print(f"  - Height: {data['height']} ft")
    print("\n  - Moves:")
    moves_list = [move['move']['name'] for move in data['moves'][:5]]  # Show top 5 moves
    print("    " + ", ".join(moves_list))
    print("\n  - Abilities:")
    abilities_list = [ability['ability']['name'] for ability in data['abilities']]
    print("    " + ", ".join(abilities_list))
    print("\n  - Types:")
    types_list = [type_info['type']['name'] for type_info in data['types']]
    print("    " + ", ".join(types_list))
    print("-" * 20)
    
    # Simple image visualization (console-based)
    print("\n") # Placeholder for visual representation

def save_pokemon_data(data):
    """
    Saves the Pokémon data to a JSON file.

    Args:
        data (dict): The JSON data of the Pokémon.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        print(f"Created directory: '{DATA_DIR}'")

    file_name = f"{data['name'].lower()}.json"
    file_path = os.path.join(DATA_DIR, file_name)

    pokemon_info = {
        "name": data['name'],
        "image_url": data['sprites']['front_default'],
        "stats": {
            "weight": data['weight'],
            "height": data['height'],
            "moves": [move['move']['name'] for move in data['moves']],
            "abilities": [ability['ability']['name'] for ability in data['abilities']],
            "types": [type_info['type']['name'] for type_info in data['types']],
        }
    }

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(pokemon_info, f, indent=4)
        print(f"Saved Pokémon data to '{file_path}' successfully! ")
    except IOError as e:
        print(f"Error saving file: {e}")

def main():
    """
    Main function to run the Pokédex program.
    """
    print("Welcome to your professional Pokédex! ")
    while True:
        pokemon_name = input("\nEnter the name of a Pokémon (or 'exit' to quit): ")
        if pokemon_name.lower() == 'exit':
            print("Thanks for using the Pokédex! See you later! ")
            break

        print(f"Searching for '{pokemon_name}'...")
        pokemon_data = get_pokemon_data(pokemon_name)

        if pokemon_data:
            display_pokemon_info(pokemon_data)
            save_pokemon_data(pokemon_data)
            
        print("-" * 30)

if __name__ == "__main__":
    main()