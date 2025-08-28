import csv

video_games = []

print("Ingrese los datos de los videojuegos. Escriba 'exit' en el nombre para terminar.")

def game_input ():

    title = input("Ingrese el nombre del video juego: ")
    if title.lower() == 'exit':
        return None
    genre = input("Ingrese el genero del videojuego: ")
    developer = input("Ingrese el nombre del desarrollador del videojuego: ")
    classification = input("Ingrese la clasificacion ESRB del videojuego: ")

    return {
        'Nombre': title,
        'Genero': genre,
        'Desarrollador': developer,
        "Clasificacion ESRB": classification

    }
def game_check (target_list):
    while True:
        game = game_input()
        if game is None:
            break
        target_list.append(game)

videogames_headers = [
    'Nombre',
    'Genero',
    'Desarrollador',
    'Clasificacion ESRB'
]

def write_game_file(file_path, data, headers):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

def save_game(data, headers):
    if data:
        write_game_file('videogames.csv', data, headers)
        print(f" Saved {len(data)} game(s) to 'videogames.csv'.")
    else:
        print("No games entered. File was not created.")

if __name__ == "__main__":
    game_check(video_games)
    save_game(video_games, videogames_headers)

