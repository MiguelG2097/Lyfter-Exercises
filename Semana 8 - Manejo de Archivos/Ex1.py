
def read_songs(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        songs = file.readlines()

    songs.sort()

    with open(output_file, "w",encoding='utf-8') as file:
        for song in songs:
            file.write(song + '\n')
    print(f"Canciones ordenadas")

read_songs('songs.txt', 'sort_songs.txt')