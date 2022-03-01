from moviepy.editor import *

mp4 = input('Which video you want to change to mp3 :')
mp3 =input('Enter mp3 name :')

mp4clip = VideoFileClip(mp4)
mp3clip = mp4clip.audio

mp3clip.write_audiofile(mp3)
mp3clip.close()
mp4clip.close()

# https://youtu.be/u5x5RZNtOqE
