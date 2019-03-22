import pafy
import download

def downloadLink(url,id=-1):
    video = pafy.new(url)
    streams=video.streams
    name=video.title
    # print("Available Streams:")
    # for stream in streams:
    #     print(stream.resolution,stream.extension, stream.get_filesize())
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


def main(URL,location,playListSupport):
    if  playList(URL) and playListSupport=="True":
        wholePlaylist(URL,location)
    else:
        URL,name,length=downloadLink(URL)
        download.youtube_Download_File(URL,location,name,length)
