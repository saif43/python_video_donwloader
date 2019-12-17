import pytube

video_url = input('Enter Youtube video link: ') # paste here your Youube videos' url
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('')