class Song:
    """ Class to represent Song
    Attributes:
        title (str) : The title of the song
        artist (str): An Artist on name of song representing the song creator:
        duration (int): The duration of the song in seconds
    """

    def __init__(self, title, artist, duration=0):
        """ Song init method
        :param title: Initialises the 'title' attribute
        :param artist: At Artist object representing the song's creator.
        :param duration (Optional[int]): Initial value for the 'duration' attribute. Default to zero if not specified
        """
        self.title = title
        self.duration = duration
        self.artist = artist

    def get_title(self):
        return self.title

    name = property(get_title)


class Album:
    """
        Class to represent an Album, using its track list
        Attribute:
        name (str): The name of the album
        year (int) : The year album was relased
        artist (str) :  The artist responsible for the album. If not specified the artist will
        default to an artist with the name "unknown".
        tracks (List[song]) : A list of the songs on the album

        Methods:
            add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name , year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Unkown"
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """
        Add a song to the track list
        :param song: A song to add
        :param position: (Optional[int]) : If specified , the song will be added to the position
        in the track list - inserting it between other song if necessary.otherwise, the song will be
        added to the end of the list

        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    """ Basic calss to store artist details.

    Arrtibutes:
        name (str): The name of the artist.
        albums (List[Album]) : A list of the album by this artist.
        The list includes inly those albums in this collection, it is not an exhaustive
        list of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's album list
    """
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """ Add a new album to the list.

        Args:
            album (ALbum) : Album object to the list.
                If the album is already present, ti will not added again
        :param album:
        :return:
        """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """
        Add a new song to the collection of albums.
        This method will add the song to an album in this collection.
        A new album will be created in the collection if it doesnt already exist
        :param name:
        :param year:
        :param title:
        :return:
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print(" Found album "+ name)

        album_found.add_song(title)


def find_object(field, object_list):
    """
    check 'object_list' to see if an object with a 'name; attirbute qual to 'field' exists,
    return it if so
    """
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    artist_list = []

    with open("albums.txt", 'r') as albums:
        for line in albums:
            # data row should consit of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            #new_artist.add_song(album_field, year_field, song_field)


    return artist_list


def create_checkfile(artist_list):
    """ create a check file from the object data for comparision with the original file"""
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song), file=checkfile)

if __name__ == '__main__':
    artists = load_data()
    print(" There are {} artists ".format(len(artists)))

    create_checkfile(artists)