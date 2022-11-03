import youtube_dl
import ffmpeg
import os

SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Downloads'

def converter(_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl':SAVE_PATH + f'/%(playlist_title)s - Downloaded Songs/%(title)s.%(ext)s',
        'quiet': True,
        'ignoreerrors': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([_url])
if __name__ == "__main__":
    vidURL = input("What is the link of the video/playlist? Make sure if it is playlist to make it public!\n>")
    print("\nAll files will be saved in Downloads.\nDownloading files now... Please wait.\nIf you close this program, simply use the same link again to continue download sequence.\n")
    converter(vidURL)