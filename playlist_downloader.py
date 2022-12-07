import os
import mutagen
from pytube import Playlist


def downloader(links):

    for link in links:
        owd = os.getcwd()
        playlist = Playlist(link)
        os.mkdir(playlist.title)
        os.chdir(playlist.title)

        for video in playlist.videos:
            out_file = video.streams.filter(only_audio=True,
                                            subtype="mp4").order_by("abr").last().download()
            new_file = out_file[:-4] + ".mp3"
            os.rename(out_file, new_file)

            try:
                meta = mutagen.easyid3.EasyID3(new_file)
            except:
                meta = mutagen.File(new_file, easy=True)
                meta.add_tags()

            meta["title"] = video.title
            meta["artist"] = video.author[:-8]

            meta.save(new_file)
            print(new_file + " saved.")

        os.chdir(owd)

if __name__=="__main__":
    links = []

    downloader(links)
