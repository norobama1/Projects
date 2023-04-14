from pytube import YouTube

def Downloader(link):
    yt = YouTube(link)
    print("Title: ", yt.title)
    print("View: ", yt.views)
    youtubeObject = yt.streams.get_highest_resolution()
    try:
        youtubeObject.download('./Youtube')
    except:
        print("An error has occurred")
    print("Download is completed successfully")

link = input("Enter the video link you want to download: ")
Downloader(link)