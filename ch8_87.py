#Album

def make_album(artist_name, album_title, trucks=''):
    artist_dict = {'name' : artist_name, 'album title' : album_title}
    if trucks:
        artist_dict['trucks'] = trucks
    return artist_dict

artist = make_album('michael jackson', 'Forever')
print(artist)
artist2 = make_album('bob marley', 'legend', 21)
print(artist2)
artist3 = make_album('damian marley', 'Halfway three')
print(artist3)