import pafy
import download

def downloadLink(url):
    video = pafy.new(url)
    streams=video.streams
    name=video.title
    print("Available Streams:")
    for stream in streams:
        print(stream.resolution,stream.extension, stream.get_filesize())
    id=int(input("Enter Index(Enter -1 for best)"))
    length=-1
    if id ==-1:
        best=video.getbest()
        URL=best.url
        length=best.get_filesize()
        extension=best.extension
    else:
        URL=streams[id].url
        length=streams[id].get_filesize()
        extension=streams[id].extension 
    return URL,name+"."+extension,length

def playList(url):
    playList=pafy.get_playlist(url)
    if len(playList['items'])>1:
        return True
    return False


def wholePlaylist(URL,location):
    Objects=pafy.get_playlist2(URL)
    for obj in Objects:
        name=obj.title
        best=obj.getbest()
        URL=best.url
        length=best.get_filesize()
        extension=best.extension
        download.youtube_Download_File(URL,location,name+"."+extension,length)




def main():
    URL=input("URL")
    location=input("Location")
    if playList(URL):
        print("This video is part of PlayList. Do you want to download whole play List(YES/NO):", end=" ")
        ans=input()
        if ans=='YES':
            wholePlaylist(URL,location)
        else:
            URL,name,length=downloadLink(URL)
            download.youtube_Download_File(URL,location,name,length)


if __name__ == "__main__":
    main()


