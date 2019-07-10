import pytube
v = "https://www.youtube.com/watch?v=1I-3vJSC-Vo"
yt = pytube.YouTube(v)
vid = yt.streams.first()
vid.download("//Users//dheerajasnani//Desktop")