import re
import urllib.request
from bs4 import BeautifulSoup
import sys
from Naked.toolshed.shell import execute_js,muterun_js

artist = sys.argv[1]
title = sys.argv[2]
stuff = get_lyrics(artist,title)
print(stuff)
# TODO make a couple types of output, (HTML)(CLEAN LINES)(UNIQUE LINES)(PURE STRING)
# maybe lets do some analysis stuff? Unique words? vocabulary?






def get_lyrics(artist,song_title):
    artist = artist.lower()
    song_title = song_title.lower()
    # remove all except alphanumeric characters from artist and song_title
    artist = re.sub('[^A-Za-z0-9]+', "", artist)
    song_title = re.sub('[^A-Za-z0-9]+', "", song_title)
    if artist.startswith("the"):    # remove starting 'the' from artist e.g. the who -> who
        artist = artist[3:]
    url = "http://azlyrics.com/lyrics/"+artist+"/"+song_title+".html"
    
    try:
        content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(content, 'html.parser')
        lyrics = str(soup)
        # lyrics lies between up_partition and down_partition
        up_partition = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
        down_partition = '<!-- MxM banner -->'
        lyrics = lyrics.split(up_partition)[1]
        lyrics = lyrics.split(down_partition)[0]
        lyrics = lyrics.replace('<br>','').replace('</br>','').replace('</div>','').strip()
        return lyrics
    except Exception as e:
        print("Exception occurred \n" +str(e))
        sys.exit()
'''
for line in stuff2:
    line = line.strip("\n")
    if line.strip():
        verse.append(line)
    else:
        tooAdd = verse.copy()
        verses.append(tooAdd)
        verse = []
#title = title.replace("/","-")
fileName = artist+"-"+title+".txt"
f = open(fileName,"w")
for verse in verses:
    f.write("\n")
    for line in verse:
        line = line.replace("[","")
        line = line.replace("]","")
        line = BeautifulSoup(line)
        f.write(line.get_text()+"\n")
f.close()

resp = muterun_js('uploader.js',fileName+" "+title+" "+artist)
if(resp.exitcode == 0):
    print("python-success")
    print(resp.stdout)


else:
    print("python-fail")
    print(resp.stderr)
'''