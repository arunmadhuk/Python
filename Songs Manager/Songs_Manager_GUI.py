from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from operator import (eq, lt)

import os
import mp3_tagger
import re
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import time

tk = Tk()
# dir = filedialog.askdirectory()
tk.geometry('430x50')
tk.title("Songs Organizer")


# Change the mp3 file name into "Track NO + Song Title"
def filenamechanger(song_path, songtitle, album_name, songtrackno):
    new_filename = songtrackno.zfill(2) + ' - ' + songtitle + '.mp3'
    # album_directory = os.path.join(songs_directory, album_name.split('\0', 1)[0])
    # print('New File Name is ', new_filename)
    global songs_directory

    new_filepath = os.path.join(songs_directory, new_filename)
    # print(new_filepath)
    if not os.path.exists(new_filepath):
        os.rename(song_path, new_filepath)
    # if os.path.exists(new_filepath):
    # print(new_filename, ' exists already.')


#  song_info = [song_path, song_album, album_composer, song_year, song_title, song_artist, song_track_no, song_genre ]
def prefixremover(song_info, prefix):
    # print('prefixremover',song_title)
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
    mp3_newinfo.save()
    time.sleep(1)
    filenamechanger(song_info[0], new_song_title, new_album_name, song_info[6])


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
    mp3_newinfo_1.save()
    time.sleep(1)
    filenamechanger(song_info[0], new_song_title, new_album_name, song_info[6])


def songinfoupdater(song_path):
    mp3 = MP3File(song_path)

    # Remove ID3 Tag V1 & V2 from Song Album
    tag_album = mp3.album
    # print(tag_album)
    tag_album_2 = str(tag_album).split('[ID3TagV2(album:')
    song_album, v1album = str(tag_album_2[1]).split('), ID3TagV1(album:')
    # print(song_album)

    # Remove ID3 Tag V1 & V2 from Song Artist
    tag_artist = str(mp3.artist)  # .encode('utf-8')
    # print(tag_artist)
    tag_artist_2 = str(tag_artist).split('[ID3TagV2(artist:')
    song_artist1, v1artist = str(tag_artist_2[1]).split('), ID3TagV1(artist:')
    song_artist = song_artist1
    # print(song_artist)

    album_composer = mp3.composer
    # print(album_composer)

    # Remove ID3 Tag V1 & V2 from Song Title
    tag_song = mp3.song
    tag_song_2 = str(tag_song).split('[ID3TagV2(song:')
    song_title, title = str(tag_song_2[1]).split('), ID3TagV1(song:')
    # print(song_title)

    # Remove ID3 Tag V1 & V2 from Song Track
    tag_track = mp3.track
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

    # Remove ID3 Tag V1 & V2 from Song Genre
    tag_genre = mp3.genre

    if str(tag_genre).__contains__('ID3TagV2(genre'):
        tag_genre_2 = str(tag_genre).split('[ID3TagV2(genre:')
        song_genre, v1genre = str(tag_genre_2[1]).split('), ID3TagV1(genre:')
    # print(song_genre)

    tag_year = mp3.year
    tag_year_2 = str(tag_year).split('[ID3TagV2(year:')
    song_year, v1year = str(tag_year_2[1]).split('), ID3TagV1(year:')

    song_info = [song_path, song_album.split('\0', 1)[0], album_composer.split('\0', 1)[0], song_year.split('\0', 1)[0],
                 song_title.split('\0', 1)[0], song_artist.split('\0', 1)[0], song_track_no.split('\x00', 1)[0],
                 song_genre.split('\0', 1)[0]]

    if "[SunStarMusiQ.Com] " in song_title:
        prefixremover(song_info, "[SunStarMusiQ.Com] ")

    if "[VStarMusiQ.Com] " in song_title:
        prefixremover(song_info, "[VStarMusiQ.Com] ")

    if "[VStarMusiq.Com] " in song_title:
        prefixremover(song_info, "[VStarMusiq.Com] ")

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
        suffixremover(song_info, " - www.123musiq.com -  ® Riya collections ®")

    if " - VmusiQ.Com" in song_title:
        suffixremover(song_info, " - VmusiQ.Com")

    if "- TamilWire.com" in song_title:
        suffixremover(song_info, "- TamilWire.com")

    if "-MassTamilan.com" in song_title:
        suffixremover(song_info, "-MassTamilan.com")

    if "- [Masstamilan.in]" in song_title:
        # print('got')
        suffixremover(song_info, "- [Masstamilan.in]")

    if " [Masstamilan.in]" in song_title:
        # print('got')
        suffixremover(song_info, " [Masstamilan.in]")

    if "::Singamda.Com:: " in song_title:
        suffixremover(song_info, "::Singamda.Com:: ")

    else:
        # continue
        filenamechanger(song_path, song_title, song_album, song_track_no)


def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


# Checks the mp3 files and displays the Album Name, Composer, Year & Genre Details
def albumdetailsloader(directory):
    # tkinter.messagebox.showinfo("Hello Title", directory)
    # txt_path.insert(index=0, string=directory)
    song_info = []
    for subdir, dirs, mp3_files in os.walk(directory):
        for mp3file in mp3_files:
            if mp3file.endswith('.mp3'):
                song_path = subdir + os.sep + mp3file
                songs_folder = subdir
                file_info = os.stat(song_path)
                file_size = convert_bytes(file_info.st_size)
                if file_size.__contains__('MB'):
                    print('song path', song_path)
                    if os.path.exists(song_path):
                        try:
                            mp3 = MP3File(song_path)
                            # Remove ID3 Tag V1 & V2 from Song Album
                            tag_album = mp3.album
                            tag_album_2 = str(tag_album).split('[ID3TagV2(album:')
                            song_album, v1album = str(tag_album_2[1]).split('), ID3TagV1(album:')
                            # Remove ID3 Tag V1 & V2 from Song Artist
                            tag_artist = str(mp3.artist)  # .encode('utf-8')
                            tag_artist_2 = str(tag_artist).split('[ID3TagV2(artist:')
                            song_artist1, v1artist = str(tag_artist_2[1]).split('), ID3TagV1(artist:')
                            song_artist = song_artist1
                            album_composer = mp3.composer
                            # Remove ID3 Tag V1 & V2 from Song Genre
                            tag_genre = mp3.genre
                            if str(tag_genre).__contains__('ID3TagV2(genre'):
                                tag_genre_2 = str(tag_genre).split('[ID3TagV2(genre:')
                                song_genre, v1genre = str(tag_genre_2[1]).split('), ID3TagV1(genre:')

                            tag_year = mp3.year
                            tag_year_2 = str(tag_year).split('[ID3TagV2(year:')
                            song_year, v1year = str(tag_year_2[1]).split('), ID3TagV1(year:')

                            song_info.append([song_album.split('\0', 1)[0], album_composer.split('\0', 1)[0],
                                              song_year.split('\0', 1)[0],
                                              song_genre.split('\0', 1)[0]])

                        except:
                            # tkinter.messagebox.showinfo("Error", song_path + " can't update tag information. Check Manually")
                            # print()
                            pass
                            # input('Press any key to continue')
                        continue
                else:
                    continue

    length = len(song_info)
    alb_name = []
    alb_comp = []
    alb_genre = []
    alb_year = []

    for a in range(length):
        alb_name.append(song_info[a][0])
        alb_comp.append(song_info[a][1])
        alb_year.append((song_info[a][2]))
        alb_genre.append(song_info[a][3])

    alb_unique = set(alb_name)
    alb_comp_unique = set(alb_comp)
    alb_year_unique = set(alb_year)
    alb_genre_unique = set(alb_genre)

    for a in alb_unique:
        if len(alb_unique) > 1:
            txt_albumname.insert(index=0, string="; ")
        txt_albumname.insert(index=0, string=a.strip())

    for ab in alb_comp_unique:
        if len(alb_comp_unique) > 1:
            txt_composer.insert(index=0, string="; ")
        txt_composer.insert(index=0, string=ab.strip())

    for ac in alb_year_unique:
        if len(alb_year_unique) > 1:
            txt_year.insert(index=0, string="; ")
        txt_year.insert(index=0, string=ac.strip())

    for ad in alb_genre_unique:
        if len(alb_genre_unique) > 1:
            txt_genre.insert(index=0, string="; ")
        txt_genre.insert(index=0, string=ad.strip())

#UI during App starting
def startupui():
    # SongsPath
    tk.geometry('430x50')
    lbl_path = Label(tk, text="Songs Path:", font="Calibri 13")
    lbl_path.place(x=10, y=10)
    btn_selectDirectory = Button(tk, text="...", font="Calibri 11", command=btndirectoryselect)
    btn_selectDirectory.place(x=370, y=12)
    txt_path.place(x=110, y=13)

# UI for valid songs folder
def songsupdaterui():
    # Update Button
    tk.geometry('430x200')
    btn_updatesongs.place(x=250, y=163)
    # AlbumName
    lbl_albumname.place(x=10, y=43)
    txt_albumname.place(x=110, y=45)
    # AlbumComposer
    lbl_composer.place(x=10, y=70)
    txt_composer.place(x=110, y=73)
    # Genre
    lbl_genre.place(x=10, y=100)
    txt_genre.place(x=110, y=103)
    # Year
    lbl_year.place(x=10, y=130)
    txt_year.place(x=110, y=133)


def isgivendirectoryhasmp3(directory):
    global files
    files = 0
    for subdir, dirs, mp3_files in os.walk(directory):
        for mp3file in mp3_files:
            if mp3file.endswith('.mp3'):
                files = files + 1

    if files >= 1:
        songsupdaterui()
        txt_path.delete(0, END)
        txt_path.insert(index=0, string=directory)
        albumdetailsloader(directory)

    if files == 0:
        tkinter.messagebox.showinfo("Invalid Folder", " No valid mp3 files found")
        startupui()


def givendirectorychecker(songsdirectory):
    for subdir, dirs, mp3_files in os.walk(songsdirectory):
        for mp3file in mp3_files:
            if mp3file.endswith('.mp3'):
                song_path = subdir + os.sep + mp3file
                songs_folder = subdir
                file_info = os.stat(song_path)
                file_size = convert_bytes(file_info.st_size)
                if file_size.__contains__('MB'):
                    print('song path', song_path)
                    if os.path.exists(song_path):
                        try:
                            songinfoupdater(song_path)
                        except:
                            # print()
                            pass
                            # input('Press any key to continue')
                continue
            else:
                continue


def btnupdatesongs():
    givendirectorychecker(songs_directory)


def btndirectoryselect():
    global songs_directory
    songs_directory = filedialog.askdirectory()
    isgivendirectoryhasmp3(songs_directory)


songs_directory = r"C:"
files = 0
lbl_path = Label(tk, text="Songs Path:", font="Calibri 13")
txt_path = Entry(tk, width=30, font="Calibri 12")
btn_updatesongs = Button(tk, text="Update", font="Calibri 12", command=btnupdatesongs)
lbl_albumname = Label(tk, text="Album:", font="Calibri 13")
txt_albumname = Entry(tk, width=30, font="Calibri 12")
lbl_composer = Label(tk, text="Composer:", font="Calibri 13")
txt_composer = Entry(tk, width=30, font="Calibri 12")
lbl_genre = Label(tk, text="Genre:", font="Calibri 13")
txt_genre = Entry(tk, width=30, font="Calibri 12")
lbl_year = Label(tk, text="Year:", font="Calibri 13")
txt_year = Entry(tk, width=30, font="Calibri 12")

startupui()

tk.mainloop()
