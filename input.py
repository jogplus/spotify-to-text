import api_interact

def create_song_list():
    try:
        file = open('songs.txt', 'r')
        tracks = file.read().splitlines()
        songs = []
        for song in tracks:
            songs.append(song[14:])
        return songs
    finally:
        if file != None:
            file.close()

def update_output_file(track_list, output_file):
    for track in track_list:
        try:
            if track == ', ':
                pass
            else:
                output_file.write(track)
                output_file.write('\n')
        except UnicodeEncodeError:
            pass

def create_output_file():
    try:
        output_file = open('output.txt', 'r')
        output_file = open('output.txt', 'a')
        print('output.txt found')
        return output_file
    except FileNotFoundError:
        print('output.txt not found')
        print('creating output.txt...')
        output_file = open('output.txt', 'w+')
        return output_file

def main():
    output_file = create_output_file()
    songs = create_song_list()
    track_list = api_interact.generate_track_list(songs, [])
    update_output_file(track_list, output_file)

if __name__ == '__main__':
    main()