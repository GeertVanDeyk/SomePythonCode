class Song:

    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song
        
    def is_repeating_playlist(self):
           CompletePlayList_dict = {} # build a dictionary keeping track of all checked songs
           CheckedSong = self         # the song calling the function is the first to be checked if it has a next song defined  
           while True:                # this creates an eternal loop allowing for all songs to be checked
             try:                     # the try block will generate an error if the CheckedSong.next.name results in a Nonetype (indicating there is no next song defined)   
              if CheckedSong.next.name in CompletePlayList_dict:
                 return True          # next song is already in the playlist, therefore the list will repeat itself  
             except:                   
                 return False         # next song has not been defined, therefore the playlist is NOT repeating 
             CompletePlayList_dict[CheckedSong.name] = CheckedSong.name # Add checked song to playlist
             CheckedSong = CheckedSong.next # take the next song as song for checking
            
          
        
            
first = Song("Hello")
second = Song("Eye of the tiger")
third = Song("Living on a prayer")

    
first.next_song(second);
second.next_song(third);


   
print(first.is_repeating_playlist())
