import os
import mp3_tagger
import re
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import time


songs_directory = "D:\Mp3-Tag"


def filenamechanger(song_path, songtitle, songtrackno):
    new_filename = songtrackno.zfill(2) + ' - ' + songtitle + '.mp3'
    new_filepath = os.path.join(songs_directory, new_filename)
    print(song_path)
    print(new_filepath)
    if os.path.exists(new_filepath):
        newfilename = songtrackno.zfill(2) + ' - ' + songtitle + '- 1.mp3'
        newpath = os.path.join(songs_directory, newfilename)
        os.rename(song_path,newpath)
    else:
        os.rename(song_path, new_filepath)

#  song_info = [song_path, song_album, album_composer, song_year, song_title, song_artist, song_track_no, song_genre ]
def prefixremover(song_info, prefix):
    #print('prefixremover',song_title)
    name = song_info[4].split(prefix)
    new_song_title = re.sub('[^ a-zA-Z0-9]', '', name[1])

    if str(song_info[5]).__contains__(prefix):
        artist = song_info[5].split(prefix)
        new_song_artist = artist[1]
    else:
        new_song_artist = song_info[5]

    if str(song_info[1]).__contains__(prefix):
        album = song_info[1].split(prefix)
        new_album_name = re.sub('[^ a-zA-Z0-9]', '', album[1])
    else:
        new_album_name = song_info[1]

    if str(song_info[2]).__contains__(prefix):
        composer = song_info[2].split(prefix)
        new_album_composer = composer[1]
    else:
        new_album_composer = song_info[2]

    mp3_newinfo = MP3File(song_info[0])
    mp3_newinfo.song = new_song_title
    mp3_newinfo.artist = new_song_artist
    mp3_newinfo.album = new_album_name
    mp3_newinfo.composer = new_album_composer
    mp3_newinfo.band = new_album_composer
    mp3_newinfo.track = song_info[6]
    #mp3_newinfo.copyright = ''
    #mp3_newinfo.comment = ''
    #mp3_newinfo.publisher = ''
    print(new_song_title)
    print(new_song_artist)
    print(new_album_name)
    print(new_album_composer)
    print(song_info[6])
    print(song_info[7])
    #input('Press any key to continue')
    mp3_newinfo.save()
    time.sleep(1)
    filenamechanger(song_info[0], new_song_title, song_info[6])


def suffixremover(song_info, suffix):
    name = song_info[4].split(suffix)
    new_song_title = re.sub('[^ a-zA-Z0-9]', '', name[0])
    if str(song_info[5]).__contains__(suffix):
        artist = song_info[5].split(suffix)
        new_song_artist = artist[0]
    else:
        new_song_artist = song_info[5]
    if str(song_info[1]).__contains__(suffix):
        album = song_info[1].split(suffix)
        new_album_name = re.sub('[^ a-zA-Z0-9]', '', album[0])
    else:
        new_album_name = song_info[1]

    if str(song_info[2]).__contains__(suffix):
        composer = song_info[2].split(suffix)
        new_album_composer = composer[0]
    else:
        new_album_composer = song_info[2]

    mp3_newinfo_1 = MP3File(song_info[0])
    mp3_newinfo_1.song = new_song_title
    mp3_newinfo_1.artist = new_song_artist
    mp3_newinfo_1.album = new_album_name
    mp3_newinfo_1.composer = new_album_composer
    mp3_newinfo_1.band = new_album_composer
    mp3_newinfo_1.track = song_info[6]
    #mp3_newinfo_1.copyright = ''
    #mp3_newinfo_1.comment = ''
    #mp3_newinfo_1.publisher = ''
    print(new_song_title)
    print(new_song_artist)
    print(new_album_name)
    print(new_album_composer)
    print(song_info[6])
    print(song_info[7])
    #input('Press any key to continue')
    mp3_newinfo_1.save()
    time.sleep(1)
    #filenamechanger(song_info[0], new_song_title, song_info[6])



def songinfoupdater(song_path):

        mp3 = MP3File(song_path)
        # Remove ID3 Tag V1 & V2 from Song Album
        tag_album = mp3.album
        tag_album_2 = str(tag_album).split('[ID3TagV2(album:')
        song_album, v1album = str(tag_album_2[1]).split('), ID3TagV1(album:')

        # Remove ID3 Tag V1 & V2 from Song Artist
        tag_artist = str(mp3.artist).encode('utf-8')
        #print(str(tag_artist).encode('ISO-8859-1'))
        #print(tag_artist)
        tag_artist_2 = str(tag_artist).split('[ID3TagV2(artist:')
        song_artist1, v1artist = str(tag_artist_2[1]).split('), ID3TagV1(artist:')
        song_artist = song_artist1

        album_composer = mp3.composer

        # Remove ID3 Tag V1 & V2 from Song Title
        tag_song = mp3.song
        tag_song_2 = str(tag_song).split('[ID3TagV2(song:')
        song_title, title = str(tag_song_2[1]).split('), ID3TagV1(song:')

        # Remove ID3 Tag V1 & V2 from Song Track
        tag_track = mp3.track
        tag_track_2 = str(tag_track).split('[ID3TagV2(track:')
        if tag_track_2[1].__contains__('/'):
           song_track_no, trackno = str(tag_track_2[1]).split('/0')
        else:
            song_track_no, v1trackno = str(tag_track_2[1]).split('), ID3TagV1(track:')

        # Remove ID3 Tag V1 & V2 from Song Genre
        tag_genre = mp3.genre
        if str(tag_genre).__contains__('ID3TagV2(genre'):
            tag_genre_2 = str(tag_genre).split('[ID3TagV2(genre:')
            song_genre, v1genre = str(tag_genre_2[1]).split('), ID3TagV1(genre:')

        # Remove ID3 Tag V1 & V2 from Song Year
        tag_year = mp3.year
        tag_year_2 = str(tag_year).split('[ID3TagV2(year:')
        song_year, v1year = str(tag_year_2[1]).split('), ID3TagV1(year:')

        song_info = [song_path, song_album, album_composer, song_year, song_title, song_artist, song_track_no, song_genre ]

        if "[SunStarMusiQ.Com] " in song_title:
            prefixremover(song_info, "[SunStarMusiQ.Com] ")

        if '::Singamda.Com::' in song_title:
            suffixremover(song_info, "::Singamda.Com::")

        if "-StarMusiQ.Fun" in song_title:
            suffixremover(song_info, "-StarMusiQ.Fun")

        if "-MassTamilan.org" in song_title:
            suffixremover(song_info, "-MassTamilan.org")

        if "-StarMusiQ.Com" in song_title:
            suffixremover(song_info, '-StarMusiQ.Com')

        if "-TamilMovieSongs.IN" in song_title:
            suffixremover(song_info, '-TamilMovieSongs.IN')

        if "-VmusiQ.Com" in song_title:
            suffixremover(song_info, '-VmusiQ.Com')

        if "-TamilMovieSongs.IN" in song_title:
            suffixremover(song_info, '-TamilMovieSongs.IN')

        if " - MassTamilan.com" in song_title:
            suffixremover(song_info, '- MassTamilan.com')


        #else:
            #continue
            #filenamechanger(song_path, song_title, song_track_no)



songinfoupdater(r'D:\Mp3-Tag\Kurangu_Bommai\Annamaare_Ayyamaare-5StarMusiQ.Com.mp3')
#filepath = "D:\Mp3-Tag\Ullathai_Killadhae-VmusiQ.Com.mp3"
#songinfoupdater (filepath)

def convert_bytes(num):

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def folderregressionchecker(songs_directory):
    for subdir, dirs, mp3_files in os.walk(songs_directory):
        for mp3file in mp3_files:
           if mp3file.endswith('.mp3'):
               #print(mp3file)
               song_path = subdir + os.sep + mp3file
               songs_folder = subdir
               #print(songs_folder)
               file_info = os.stat(song_path)
               file_size = convert_bytes(file_info.st_size)
               if file_size.__contains__('MB'):
                   #print(song_path)
                   if isfileExists(song_path):
                       print(song_path)
                       try:
                           songinfoupdater(song_path)
                       except IOError:
                           print(song_path , " can't update tag information. Check Manually")
                           input('Press any key to continue')
               continue
           else:
                continue


songs_directory = r"D:\Mp3-Tag\Kurangu_Bommai"
#folderregressionchecker(songs_directory)