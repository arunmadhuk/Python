import os
from filecmp import dircmp
import csv


def emptyfolderdeletor(songsdirectory):
    #for subdir, dirs, mp3_files in os.walk(songsdirectory):
    for subdir, dirs, mp3_files in os.walk(songsdirectory):
        print(subdir)
        print(mp3_files)

        for mp3file in mp3_files:

            if not mp3file.endswith('.mp3') or mp3file.endswith('.Mp3'):
                deletefile = subdir + os.sep + mp3file
                print(deletefile)
                os.remove(deletefile)

        if [f for f in os.listdir(subdir) if not f.startswith('.')] == []:
            print("empty")
            os.rmdir(subdir)
        else:
            print("not empty")


def print_diff_files(dcmp):

    for name in dcmp.diff_files:
       print (name, dcmp.left, dcmp.right)

    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)

songs_directory = r"D:\Arun Madhu\Songs"

#emptyfolderdeletor(songs_directory)

updated_songs_directory = r"D:\Arun Madhu\Songs"
source_songs_directory = r"D:\Tamil Songs"
csvdata = []
csvdata.append(["Updated Songs Folder", "Folder Length","Album Name", "Source Songs Folder", "Folder Length" ])
dir_list = next(os.walk(updated_songs_directory))[1]

try:
    for subfolder in dir_list:
        sub_updated_songs_fodler = updated_songs_directory + os.sep + subfolder
        #sub_updated_songs_fodler = updated_songs_directory + os.sep+ subfolder
        sub_source_songs_folder = source_songs_directory + os.sep + subfolder
        #dcmp = dircmp(sub_updated_songs_fodler, sub_source_songs_folder)
        #print_diff_files(dcmp)
        sub_folder_list = next(os.walk(sub_source_songs_folder))[1]
        print(sub_updated_songs_fodler)
        if len(sub_folder_list)==0:
            #sub_updated_songsfolder = sub_updated_songs_fodler + os.sep + songsfolder
            #sub_source_songsfolder = sub_source_songs_folder + os.sep + songsfolder
            updated_songs = next(os.walk(sub_updated_songs_fodler))[2]
            source_songs = next(os.walk(sub_source_songs_folder))[2]
            print(subfolder)
            csvdata.append([sub_updated_songs_fodler, len(updated_songs), str(subfolder), sub_source_songs_folder, len(source_songs), source_songs,updated_songs])

        if not len(sub_folder_list)==0:
            for songsfolder in sub_folder_list:
                try:
                    sub_updated_songsfolder = sub_updated_songs_fodler+os.sep+songsfolder
                    sub_source_songsfolder = sub_source_songs_folder + os.sep + songsfolder
                    updated_songs = next(os.walk(sub_updated_songsfolder))[2]
                    source_songs = next(os.walk(sub_source_songsfolder))[2]
                    csvdata.append([sub_source_songsfolder, len(source_songs) , songsfolder, sub_updated_songsfolder, len(updated_songs) , source_songs, updated_songs ])
                    #print(sub_source_songsfolder, len(updated_songs))
                    #print(sub_updated_songsfolder, len(source_songs))
                    #print('---------------------------------------------------------------------------')
                except:
                    pass
        #input('Enter')
except:
    pass

csvfile = open('test.csv','w')
with csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csvdata)
print('test.csv file created')




