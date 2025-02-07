class MusicLibrary():
    def __init__(self):
        self.library = []

    def add_track(self, artist, title):
        if isinstance(artist, str) and isinstance(title, str):
            track = {"artist" : artist, "title" : title}
            self.library.append(track)
            return "Success"
        else:
            raise ValueError("Input track artist and title must be strings")
    
    def list_library(self):
        return self.library