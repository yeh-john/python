from moviepy.editor import *

mp4 = input('Which video you want to change :')
mp3 =input('Enter mp3 name')

videoClip = VideoFileClip(mp4)
audioclip = videoClip.audio

audioclip.write_audiofile(mp3)

audioclip.close()
videoClip.close()

# https://youtu.be/u5x5RZNtOqE
