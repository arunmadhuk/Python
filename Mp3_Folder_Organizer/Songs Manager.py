# Thamil MP3 songs manager will reorganize the mp3 tag information by removing the know
# prefix & suffix and also will rename the actual file names and reorganize your mp3 library

import os
import mp3_tagger
import re
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import time


def filenamechanger(song_path, songtitle, album_name, songtrackno):
    new_filename = songtrackno.zfill(2) + ' - ' + songtitle + '.mp3'
    #album_directory = os.path.join(songs_directory, album_name.split('\0', 1)[0])
    print('New File Name is ', new_filename)

    print(song_path)
    new_filepath = os.path.join(songs_directory, new_filename)
    print(new_filepath)
    if not os.path.exists(new_filepath):
        os.rename(song_path, new_filepath)
    if os.path.exists(new_filepath):
       print(new_filename, ' exists already.')


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
    #print(new_song_title)
    #print(new_song_artist)
    #print(new_album_name)
    #print(new_album_composer)
    #print(song_info[6])
    #print(song_info[7])
    mp3_newinfo.save()
    time.sleep(1)
    filenamechanger(song_info[0], new_song_title,new_album_name, song_info[6])


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
    mp3_newinfo_1.track = song_info[6].strip()
    print(new_song_title)
    print(new_song_artist)
    print(new_album_name)
    #print(new_album_composer)
    #print(song_info[6])
    #print(song_info[7])
    mp3_newinfo_1.save()
    time.sleep(1)
    filenamechanger(song_info[0], new_song_title, new_album_name, song_info[6])

def songinfoupdater(song_path):
        mp3 = MP3File(song_path)
        # Remove ID3 Tag V1 & V2 from Song Album
        tag_album = mp3.album
        #print(tag_album)
        tag_album_2 = str(tag_album).split('[ID3TagV2(album:')
        song_album, v1album = str(tag_album_2[1]).split('), ID3TagV1(album:')
        print(song_album)

        # Remove ID3 Tag V1 & V2 from Song Artist
        tag_artist = str(mp3.artist)#.encode('utf-8')
        #print(tag_artist)
        tag_artist_2 = str(tag_artist).split('[ID3TagV2(artist:')
        song_artist1, v1artist = str(tag_artist_2[1]).split('), ID3TagV1(artist:')
        song_artist = song_artist1
        #print(song_artist)

        album_composer = mp3.composer
        print(album_composer)

        # Remove ID3 Tag V1 & V2 from Song Title
        tag_song = mp3.song
        tag_song_2 = str(tag_song).split('[ID3TagV2(song:')
        song_title, title = str(tag_song_2[1]).split('), ID3TagV1(song:')
        print(song_title)

        # Remove ID3 Tag V1 & V2 from Song Track
        tag_track = mp3.track

        print(tag_track)
        if (tag_track == 32):
            song_track_no = str(1)
        if tag_track is None:
            song_track_no = str(1)

        if str(tag_track).__contains__('[ID3TagV2(track:'):
            if str(tag_track).__contains__('123'):
                song_track_no = str(1)
            else:
                tag_track_2 = str(tag_track).split('[ID3TagV2(track:')
                # print(tag_track_2)
                if tag_track_2[1].__contains__('/'):
                    song_track_no, trackno = str(tag_track_2[1]).split('/')
                else:
                    song_track_no, v1trackno = str(tag_track_2[1]).split('), ID3TagV1(track:')
        #print(song_track_no)
        # Remove ID3 Tag V1 & V2 from Song Genre
        tag_genre = mp3.genre
        #print(mp3.genre)
        #print(tag_genre)
        #input("Enter")
        if str(tag_genre).__contains__('ID3TagV2(genre'):
            tag_genre_2 = str(tag_genre).split('[ID3TagV2(genre:')
            song_genre, v1genre = str(tag_genre_2[1]).split('), ID3TagV1(genre:')
        #print(song_genre)

        # Remove ID3 Tag V1 & V2 from Song Year
        tag_year = mp3.year
        tag_year_2 = str(tag_year).split('[ID3TagV2(year:')
        song_year, v1year = str(tag_year_2[1]).split('), ID3TagV1(year:')

        song_info = [song_path, song_album.split('\0', 1)[0], album_composer.split('\0', 1)[0], song_year.split('\0', 1)[0], song_title.split('\0', 1)[0], song_artist.split('\0', 1)[0], song_track_no.split('\x00', 1)[0], song_genre.split('\0', 1)[0] ]

        print(song_info)
        input('Enter to continue')

        if "[SunStarMusiQ.Com] " in song_title:
            prefixremover(song_info, "[SunStarMusiQ.Com] ")

        if "[VStarMusiQ.Com] " in song_title:

            prefixremover(song_info,"[VStarMusiQ.Com] ")

        if "[VStarMusiq.Com] " in song_title:

            prefixremover(song_info,"[VStarMusiq.Com] ")

        if '::Singamda.Com::' in song_title:
            suffixremover(song_info, "::Singamda.Com::")

        if "-StarMusiQ.Fun" in song_title:
            suffixremover(song_info, "-StarMusiQ.Fun")

        if "-MassTamilan.org" in song_title:
            suffixremover(song_info, "-MassTamilan.org")

        if " - MassTamilan.org" in song_title:
            suffixremover(song_info, " - MassTamilan.org")

        if "-StarMusiQ.Com" in song_title:
            suffixremover(song_info, '-StarMusiQ.Com')

        if "-5StarMusiQ.Com" in song_title:
            suffixremover(song_info, "-5StarMusiQ.Com")

        if "-StarMusiQ.One" in song_title:
            suffixremover(song_info, "-StarMusiQ.One")

        if "-TamilMovieSongs.IN" in song_title:
            suffixremover(song_info, '-TamilMovieSongs.IN')

        if "-VmusiQ.Com" in song_title:
            suffixremover(song_info, '-VmusiQ.Com')

        if "-TamilMovieSongs.IN" in song_title:
            suffixremover(song_info, '-TamilMovieSongs.IN')

        if " - MassTamilan.com" in song_title:
            suffixremover(song_info, '- MassTamilan.com')

        if "-SunMusiQ.Com" in song_title:
            suffixremover(song_info, '-SunMusiQ.Com')

        if "- TMR" in song_title:
            suffixremover(song_info, "- TMR")

        if " - TamilTunes.com" in song_title:
            suffixremover(song_info, " - TamilTunes.com")

        if " - TamilMovieSongs.IN" in song_title:
            suffixremover(song_info, " - TamilMovieSongs.IN")

        if " - www.123musiq.com -  ® Riya collections ®" in song_title:
            suffixremover(song_info," - www.123musiq.com -  ® Riya collections ®")

        if " - VmusiQ.Com" in song_title:
            suffixremover(song_info," - VmusiQ.Com")

        if "- TamilWire.com" in song_title:
            suffixremover(song_info,"- TamilWire.com")

        if "-MassTamilan.com" in song_title:
            suffixremover(song_info,"-MassTamilan.com")

        if "- [Masstamilan.in]" in song_title:
            #print('got')
            suffixremover(song_info, "- [Masstamilan.in]")

        if " [Masstamilan.in]" in song_title:
            #print('got')
            suffixremover(song_info, " [Masstamilan.in]")

        if "::Singamda.Com:: " in song_title:
            print('got')
            suffixremover(song_info, "::Singamda.Com:: ")

        if "::Singamda.Com::" in song_title:
                print('got')
                suffixremover(song_info, "::Singamda.Com::")

        else:
            #continue
            filenamechanger(song_path, song_title,song_album, song_track_no)

def convert_bytes(num):

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def folderregressionchecker(songsdirectory):
    print(songs_directory)
    for subdir, dirs, mp3_files in os.walk(songsdirectory):
        #print(subdir)
        for mp3file in mp3_files:
           if mp3file.endswith('.mp3'):
               print(mp3file)
               song_path = subdir + os.sep + mp3file
               songs_folder = subdir
               #print(songs_folder)
               file_info = os.stat(song_path)
               file_size = convert_bytes(file_info.st_size)
               if file_size.__contains__('MB'):
                   print('song path', song_path)
                   if os.path.exists(song_path):
                       #print(song_path)
                       try:
                           songinfoupdater(song_path)
                       except:
                           print(song_path , " can't update tag information. Check Manually")
                           pass
                           #input('Press any key to continue')
               continue
           else:
                continue

def songsfolderorganizer(song_path, mp3file):
    try:
        mp3 = MP3File(song_path)
        # Remove ID3 Tag V1 & V2 from Song Album
        tag_album = mp3.album
        tag_album_2 = str(tag_album).split('[ID3TagV2(album:')
        song_album, v1album = str(tag_album_2[1]).split('), ID3TagV1(album:')
        album_name = str(song_album)
        tag_year = mp3.year
        print(tag_year)
        tag_year_2 = str(tag_year).split('[ID3TagV2(year:')
        song_year, v1year = str(tag_year_2[1]).split('), ID3TagV1(year:')
        if str(song_year).__contains__("), ID3TagV2(year:"):
            song_year, ye = song_year.split('), ID3TagV2(year:')
        print('Song Path', song_path)
        #album = album_name.strip()
        album = re.sub(r"\s+$", "", album_name, flags=re.UNICODE)
        print('Album', album.split('\0', 1)[0])

        year_directory = os.path.join(songs_directory, song_year.split('\0', 1)[0])
        print(year_directory)
        #input('enter')
        if not os.path.exists(year_directory):
            os.makedirs(year_directory)

        album_directory = os.path.join(year_directory, album.split('\0', 1)[0])
        #print(album.split('\0', 1)[0])
        #album_directory = re.sub('[^ ]', '', albumdirectory)
        print(album_directory)

        if os.path.exists(year_directory):
            if not os.path.exists(album_directory):
                print(album_directory)
                os.makedirs(album_directory)
        #time.sleep(1)

        newpathname = os.path.join(album_directory,mp3file)
        #print(newpathname)
        if os.path.exists(album_directory):
            print('New Path', newpathname)
            if not os.path.exists(newpathname):
                os.rename(song_path, newpathname)
    except:
        pass


def mp3filenamechanger(songsfolder):
    for subdir, dirs, mp3_files in os.walk(songsfolder):
        print("mp3 File Name:",mp3_files)
        for mp3file in mp3_files:
            if mp3file.endswith('.mp3') or mp3file.endswith('.Mp3'):
                # print(mp3file)
                song_path = songsfolder + os.sep + mp3file
                # songs_folder = subdir
                # print(songs_folder)
                print("Song Path:",song_path)
                song = MP3File(song_path)

                # Remove ID3 Tag V1 & V2 from Song Title
                tag_song = song.song
                tag_song_2 = str(tag_song).split('[ID3TagV2(song:')
                song_title, title = str(tag_song_2[1]).split('), ID3TagV1(song:')

                # Remove ID3 Tag V1 & V2 from Song Track
                tag_track = song.track
                # print(tag_track)
                if (tag_track == 32):
                    song_track_no = str(1)
                if tag_track is None:
                    song_track_no = str(1)

                if str(tag_track).__contains__('[ID3TagV2(track:'):
                    if str(tag_track).__contains__('123'):
                        song_track_no = str(1)
                    else:
                        tag_track_2 = str(tag_track).split('[ID3TagV2(track:')
                        # print(tag_track_2)
                        if tag_track_2[1].__contains__('/'):
                            song_track_no, trackno = str(tag_track_2[1]).split('/')
                        else:
                            song_track_no, v1trackno = str(tag_track_2[1]).split('), ID3TagV1(track:')

                filenamechanger(song_path,song_title.split('\0', 1)[0],"summa",song_track_no.split('\0', 1)[0])
                continue
            songsfolderorganizer(song_path, mp3file)


songs_directory = r"E:\Maanaadu"
#For Song Info Updater

#mp3filenamechanger(songs_directory)
folderregressionchecker(songs_directory)
print('--------------------------------------')
#print('Please clear the folders & wait....')
#time.sleep(10)
#print('--------------------------------------')
#input('So, have you finished deleting the folders. Then please enter to continue')
#folderchecker(songs_directory)