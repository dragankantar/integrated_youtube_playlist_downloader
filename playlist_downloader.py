import os
import mutagen
from mutagen.easyid3 import EasyID3
from pytube import Playlist


def yt_downloader(link):

    playlist = Playlist(link)
    for video in playlist.videos:
        new_file = video.title + "-" + video.author[:-8] + ".mp3"
        print("Saving: " + new_file)
        out_file = video.streams.filter(only_audio=True).first().download()
        os.rename(out_file, new_file)
        try:
            meta = EasyID3(new_file)
        except:
            meta = mutagen.File(new_file, easy=True)
            meta.add_tags()
        meta["title"] = video.title
        meta["artist"] = video.author[:-8]
        meta.save(new_file)
        print(new_file + " saved.")

def main():
    links = []
    for link in links:
        owd = os.getcwd()
        os.mkdir(link.title)
        os.chdir(link.title)
        yt_downloader(link)
        os.chdir(owd)

if __name__=="__main__":
    main()
