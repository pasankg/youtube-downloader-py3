# importing packages
from pytube import YouTube
import os

# Get url input from user
yt = YouTube(str(input("Enter the URL of the video you want to download: \n>> ")))

# File format to save
print("Enter the file format to save, mp3 or mp4 (leave blank for mp4)")
extension = str(input(">> ")) or 'mp4'

# Check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

if 'mp4' == extension:
 print('mp4')
 video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
 destination = destination + '/video'
else:
 print('mp3')
 video = yt.streams.filter(only_audio=True).first()
 destination = destination + '/audio'

# Download the file
out_file = video.download(output_path=destination)

# Set extension for mp3
if 'mp3' == extension:
 base, ext = os.path.splitext(out_file)
 new_file = base + f"{'.'}{extension}"
 os.rename(out_file, new_file) 
 print('Extension assigned.')
else:
 print('mp4 extension created.')
    
# Result of success
print(yt.title + " has been successfully downloaded.")