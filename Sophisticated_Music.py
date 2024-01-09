from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Union, List, Dict

class ValidateString:
    def __set_name__(self, instance, name):
        self.name = name

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        
        if not isinstance(value, str):
            raise ValueError(f"{self.name} should be a string")
        if value == "":
            raise ValueError(f"The {self.name} cant be Empty")
        instance.__dict__[self.name] = value

class MusicOperations(ABC):
    @abstractmethod
    def play_music(self) -> None:
        pass

    @abstractmethod
    def stop_music(self) -> None:
        pass
class AddRemoveOperrations(ABC):
    @abstractmethod
    def add_song(self, song: 'Song') -> Union['AlbumOperations', 'PlayListOperations']:
        pass
    @abstractmethod
    def remove_song(self, song: 'Song') -> Union['AlbumOperations', 'PlayListOperations']:
        pass


class AlbumOperations(ABC):
    @abstractmethod
    def show_album(self) -> List['Song']:
        pass

class PlayListOperations(ABC):
    @abstractmethod
    def show_playlist(self) -> List['Song']:
        pass

class Song(MusicOperations):
    artist = ValidateString()
    title = ValidateString()
    genre = ValidateString()
    def __init__(self, title: str, artist:str, duration: float, genre: str) -> None:
        self.artist = artist
        self.__duration = duration
        self.title = title
        self.genre = genre
        self.album = "Song without album"
    def play_music(self) -> None:
        print(f"{self.title} Song is playing...")
        # time.sleep(self.__duration)
        print("Music playback complete!")

    def stop_music(self) -> None:
        print(f"{self.title} Song is stoped")

    def get_album_name(self):
        print(self.album)



class Pop(Song):
    def __init__(self, title: str, artist: str, duration: float) -> None:
        super().__init__(title, artist, duration, genre = "Pop")

class Rock(Song):
    def __init__(self, title: str, artist: str, duration: float) -> None:
        super().__init__(title, artist, duration, genre = "Rock")

class HipHop(Song):
    def __init__(self, title: str, artist: str, duration: float) -> None:
        super().__init__(title, artist, duration, genre = "HipHop")

class Jazz(Song):
    def __init__(self, title: str, artist: str, duration: float) -> None:
        super().__init__(title, artist, duration, genre = "Jazz")

class Country(Song):
    def __init__(self, title: str, artist: str, duration: float) -> None:
        super().__init__(title, artist, duration, genre= "Country")

class Rap(Song):
    def __init__(self, title: str, artist: str, duration: float, genre: str) -> None:
        super().__init__(title, artist, duration, genre = "Rap")


class PlayList(PlayListOperations, MusicOperations, AddRemoveOperrations):
    def __init__(self, name:str, songs: List['Song']) -> None:
        self.name = name
        self.playlist_songs = songs

    def play_music(self) -> None:
        if self.playlist_songs:
            for song in self.playlist_songs:
                song.play_music()
            print("Your play list Ended")

        else:
            print("Empty PlayList, please first add music")

    def stop_music(self) -> None:
        print("Music is stoped")


    def add_song(self, song: Song) -> AlbumOperations | PlayListOperations:
        self.playlist_songs.append(song)
        return self
    
    def remove_song(self, song: Song) -> AlbumOperations | PlayListOperations:
        if self.playlist_songs:
            if song in self.playlist_songs:
                self.playlist_songs.remove(song)
                return self
            else:
                print("No such song in playlist")
                return self
        else:
            print("Empty playlist")
            return self
    
    def show_playlist(self) -> List[Song]:
        return self.playlist_songs



class Album(AlbumOperations, AddRemoveOperrations):
    artist = ValidateString()
    title = ValidateString()
    genre = ValidateString()
    def __init__(self, title:str, artist:str, relase_date:str) -> None:
        self.title = title
        self.artist = artist
        self.__relase_date = relase_date
        self.__album_songs:List['Song'] = []

    def add_song(self, song: Song) -> AlbumOperations:
        if song.album == None:
            song.album = self.title
            self.__album_songs.append(song)
            return self
        else:
            print(f"Song already belongs to {song.album} album")
            return self

    def remove_song(self, song: Song) -> AlbumOperations:
        self.__album_songs.remove(song)
        return self
    
    def show_album(self) -> List['Song']:
        return self.__album_songs

if __name__ == "__main__":
    song = Jazz("World", "Ray Charles", 2.34)
    album = Album("Holy moly", "Ray Charles", "24April")
    playlist = PlayList("Jazz", [song])
    playlist.play_music()







