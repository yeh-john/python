#import the package
from pytube import YouTube

url = input("Enter url :")
my_video = YouTube(url)

print('')
print("Vidoe title : "+my_video.title)
print('')

print('------------------------------')
print('')


'''

for stream in my_video.streams:
    print(stream)




print('')
print('Please chose ')
'''

my_video = my_video.streams.get_highest_resolution()


my_video.download('.')