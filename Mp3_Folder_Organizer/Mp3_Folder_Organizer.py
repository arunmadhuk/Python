import os
import mp3_tagger
import re
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import time


#songs_folder = r"D:\Arun Madhu\Songs\2013"


def songsfolderorganizer(song_path, mp3file):
    mp3 = MP3File(song_path)
    # Remove ID3 Tag V1 & V2 from Song Album
    tag_album = mp3.album
    tag_album_2 = str(tag_album).split('[ID3TagV2(album:')
    song_album, v1album = str(tag_album_2[1]).split('), ID3TagV1(album:')
    album_name = str(song_album)
    tag_year = mp3.year
    tag_year_2 = str(tag_year).split('[ID3TagV2(year:')
    song_year, v1year = str(tag_year_2[1]).split('), ID3TagV1(year:')
    print('Song Path', song_path)
    #album = album_name.strip()
    album = re.sub(r"\s+$", "", album_name, flags=re.UNICODE)
    print('Album', album.split('\0', 1)[0])
    album_directory = os.path.join(songs_folder, album.split('\0', 1)[0])
    #print(album.split('\0', 1)[0])
    #album_directory = re.sub('[^ ]', '', albumdirectory)
    print(album_directory)

    if not os.path.exists(album_directory):
        print(album_directory)
        os.makedirs(album_directory)
    #time.sleep(1)

    newpathname = os.path.join(album_directory,mp3file)
    #print(newpathname)
    if os.path.exists(album_directory):
        print('New Path', newpathname)
        if not os.path.exists(newpathname):
            os.rename(song_path,newpathname)




def folderregressionchecker(songsdirectory):
    #for subdir, dirs, mp3_files in os.walk(songsdirectory):
    for subdir, dirs, mp3_files in os.walk(songsdirectory):
        print(mp3_files)
        for mp3file in mp3_files:
           if mp3file.endswith('.mp3') or mp3file.endswith('.Mp3'):
               #print(mp3file)
               song_path = subdir + os.sep + mp3file
               #songs_folder = subdir
               #print(songs_folder)
               print(song_path)
               #songsfolderorganizer(song_path, mp3file)

               continue
           else:
                continue

songs_folder = r"E:\Tamil Songs\2020/Master"
folderregressionchecker(songs_folder)

#songpath = os.path.join(songs_folder,"01 - Aagaasa Veedu Kattum - MassTamilan.org.mp3")
#songsfolderorganizer(songpath,"01 - Aagaasa Veedu Kattum - MassTamilan.org.mp3")