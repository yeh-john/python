from pytube import YouTube

import time

# Downloading YouTube video

url = input("Video url :")
print("Wait a minute......")
yt = YouTube(url)
title = yt.title
streams = yt.streams.get_by_itag(22)
print("Downloading(  {}  ), wait a minute.... ".format(title))
time.sleep(1)
print("The vido download is complete.")
time.sleep(1)
print("Moving to a different directory....")
streams.download('.')
print("done")
