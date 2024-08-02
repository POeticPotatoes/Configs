import os
import random
from mutagen.mp3 import MP3
import mutagen

OSU_DIRECTORY = "/home/poeticpotato/.local/share/osu/files"
MAX_SONGS = 100

def obtain_playlist():
    playlist = []
    files = [f'{root}/{f_name}' for root, d_names, f_names in os.walk(OSU_DIRECTORY) for f_name in f_names]
    random.shuffle(files)
    for filepath in files:
        try: 
            audio = MP3(filepath)
            if (audio.info.length > 60): 
                playlist.append(filepath)
        except: pass
        if (len(playlist)>=MAX_SONGS): break
    return playlist

if __name__=="__main__":
    print("Obtaining files!")
    result = obtain_playlist()
