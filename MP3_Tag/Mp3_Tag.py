import os
import mp3_tagger
import re
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import tkinter

top = tkinter.Tk()
# Code to add widgets will go here...
#top.mainloop()

songs_directory = "D:\Mp3-Tag"


def filenamechanger(song_title, song_trackno):
    new_filename = song_trackno.zfill(2) + ' - ' + song_title + '.mp3'
    new_filepath = os.path.join(songs_directory, new_filename)
    print(song_file_path)
    print(new_filepath)
    #os.rename(song_file_path, new_filepath)


def songinfoupdater(song_path):
    mp3 = MP3File(song_path)

    # Get all tags.
    #tags = mp3.get_tags()

    # Remove ID3 Tag V1 & V2 from Song Album
    tag_album = mp3.album
    tag_album_2 = str(tag_album).split('[ID3TagV2(album:')
    song_album, v1album = str(tag_album_2[1]).split('), ID3TagV1(album:')

    # Remove ID3 Tag V1 & V2 from Song Artist
    tag_artist = mp3.artist
    tag_artist_2 = str(tag_artist).split('[ID3TagV2(artist:')
    song_artist, v1artist = str(tag_artist_2[1]).split('), ID3TagV1(artist:')

    album_composer = mp3.composer
    album_artist = mp3.band

    # Remove ID3 Tag V1 & V2 from Song Title
    tag_song = mp3.song
    tag_song_2 = str(tag_song).split('[ID3TagV2(song:')
    song_title, v1title = str(tag_song_2[1]).split('), ID3TagV1(song:')

    # Remove ID3 Tag V1 & V2 from Song Track
    tag_track = mp3.track
    tag_track_2 = str(tag_track).split('[ID3TagV2(track:')
    print(tag_track_2)
    song_track_no, v1trackno = str(tag_track_2[1]).split('), ID3TagV1(track:')
    print('song_track_no', song_track_no)
    print('v1trackno', v1trackno)

    # Remove ID3 Tag V1 & V2 from Song Genre
    tag_genre = mp3.genre
    tag_genre_2 = str(tag_genre).split('[ID3TagV2(genre:')
    song_genre, v1genre = str(tag_genre_2[1]).split('), ID3TagV1(genre:')

    # Remove ID3 Tag V1 & V2 from Song Year
    tag_year = mp3.year
    tag_year_2 = str(tag_year).split('[ID3TagV2(year:')
    song_year, v1year = str(tag_year_2[1]).split('), ID3TagV1(year:')

    tag_copyright = mp3.copyright
    tag_comment = mp3.comment

    # Remove SunStarMusiQ.Com
    if "[SunStarMusiQ.Com]" in song_title:
        name = song_title.split('[SunStarMusiQ.Com]')
        new_song_title = re.sub('[^ a-zA-Z0-9]', '', name[1])
        artist = song_artist.split('[SunStarMusiQ.Com]')
        new_song_artist = re.sub('[^ a-zA-Z0-9]', '', artist[1])
        band = album_composer.split
        mp3.song = new_song_title
        mp3.artist = new_song_artist
        mp3.copyright = ''
        mp3.comment = ''
        mp3.publisher = ''
        mp3.save()
        filenamechanger(new_song_title, song_track_no)


    if "::Singamda.Com::" in song_title:
        name = song_title.split('::Singamda.Com::')
        new_song_title = re.sub('[^ a-zA-Z0-9]', '', name[0])
        artist = song_artist.split('::Singamda.Com::')
        new_song_artist = re.sub('[^ a-zA-Z0-9]', '', artist[0])
        album = song_album.split('::Singamda.Com::')
        new_album_name = re.sub('[^ a-zA-Z0-9]', '', album[0])
        mp3.song = new_song_title
        mp3.artist = new_song_artist
        mp3.album = new_album_name
        mp3.copyright = ''
        mp3.comment = ''
        mp3.publisher = ''
        mp3.save()
        print(new_song_title)
        print(song_track_no)
        filenamechanger(new_song_title, song_track_no)

    if "-StarMusiQ.Fun" in song_title:
        name = song_title.split('-StarMusiQ.Fun')
        new_song_title = re.sub('[^ a-zA-Z0-9]', '', name[0])
        # print(''.join(e for e in filename if e.isalnum()))
        artist = song_artist.split('-StarMusiQ.Fun')
        new_song_artist = re.sub('[^ a-zA-Z0-9]', '', artist[0])
        mp3.song = new_song_title
        mp3.artist = new_song_artist
        mp3.copyright = ''
        mp3.comment = ''
        mp3.publisher = ''
        mp3.save()
        filenamechanger(new_song_title, song_track_no)

    if "-MassTamilan.org" in song_title:
        name = song_title.split('-MassTamilan.org')
        new_song_title = re.sub('[^ a-zA-Z0-9]', '', name[0])
        # print(''.join(e for e in filename if e.isalnum()))
        artist = song_artist.split('-MassTamilan.org')
        new_song_artist = re.sub('[^ a-zA-Z0-9]', '', artist[0])
        mp3.song = new_song_title
        mp3.artist = new_song_artist
        mp3.copyright = ''
        mp3.comment = ''
        mp3.publisher = ''
        # mp3.save()
        # filenamechanger(new_song_title, song_track_no)


for subdir, dirs, mp3_files in os.walk(songs_directory):
    for mp3file in mp3_files:
       if mp3file.endswith('.mp3'):
           song_file_path = subdir+os.sep+mp3file
           print(song_file_path)
           songinfoupdater(song_file_path)
           #print(subdir,os.sep, mp3file)
           input('Press Enter to Continue')
           continue
       else:
            continue

#mp3files = os.listdir(songs_directory)

#or mp3_file in mp3files:
 #   if mp3_file.endswith('.mp3'):
  #      song_file_path = os.path.join(songs_directory, os.sep,mp3_file)
   #     songinfoupdater(song_file_path)


#if (tag_song_1[0] != new_songname):
#   mp3.song = new_songname
#    mp3.save()


def hasnumber(str):
    try:
        float(str)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(str)
        return True
    except (TypeError, ValueError):
        pass


