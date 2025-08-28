import json

def read_json_file():
    with open(r"C:\Users\user\Desktop\Lyfter\Semana 8 - Manejo de Archivos\JSON\pokemon.json", 'r') as file:
        data = json.load(file)

    return data

def input_new_pokemon():
    name = input("Enter new Pokemon name: ")
    pokemon_type = input("Enter Pokemon type: ")
    hp = int(input("Enter pokemon's HP: "))
    attack = int(input("Enter pokemon's attack: "))
    defense = int(input("Enter pokemon's defense: "))
    sp_attack = int(input("Enter pokemon's Special Attack: "))
    sp_defense = int(input("Enter pokemon's Special Defense: "))
    speed = int(input("Enter pokemon's Speed: "))

    new_pokemon = {
        "name": {
            "english": name
        },
        "type": [
            pokemon_type
        ],
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }

    return new_pokemon

def store_pokemon(new_pokemon):
    data = read_json_file()
    data.append(new_pokemon)
    with open (r"C:\Users\user\Desktop\Lyfter\Semana 8 - Manejo de Archivos\JSON\pokemon.json", 'w') as f:
        json.dump(data, f, indent=4)

    
if __name__ == "__main__":
    new_pokemon = input_new_pokemon()
    store_pokemon(new_pokemon)
    print(" New Pokemon saved!")