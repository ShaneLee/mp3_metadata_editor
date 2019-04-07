import os, glob
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC

string_to_remove = input("Enter string to remove: ")
album = input("Enter Album: ")
artist = input("Enter Artist: ")

for file in glob.glob("*.mp3"):

    audio = EasyID3(file)
    tracknumber = [int(s) for s in file.split() if s.isdigit()]
    print(tracknumber)
    title = file.split(string_to_remove)[1]
    audio = EasyID3()
    audio['tracknumber'] = tracknumber
    audio['title'] = title.split('.mp3')[0]
    audio['artist'] = artist
    audio['album'] = album
    print('Saving... ' + file)
    audio.save(file)

    audio = ID3(file)
    for art in glob.glob('*.jpg'):
        with open(art, 'rb') as albumart:
            audio['APIC'] = APIC(
                              encoding=3,
                              mime='image/jpeg',
                              type=3, desc=u'Cover',
                              data=albumart.read()
                            )
    audio.save(file)
