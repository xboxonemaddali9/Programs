import youtube_dl
import ffmpeg
import os

SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Downloads'

def converter(_url, folderName):
    ydl_opts = {
        'format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
        }],
        'outtmpl':SAVE_PATH + f'{folderName} - Downloaded /%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([_url])
if __name__ == "__main__":
    vidURL = input("What is the link of the video/playlist? Make sure if it is playlist to make it public!\n>")
    folderName = input("Folder name?:\n")
    print("\nAll files will be saved in Downloads.\nDownloading files now... Please wait. It will take approximately 10 seconds per conversion.\nIf you close this program, simply use the same link again to continue download sequence.\n")
    converter(vidURL, folderName)