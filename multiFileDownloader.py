import download
import queue
import threading
import youtubeDownload
def downloader(url,location,i):
    print("Starting Download File ",str(i))
    if download.main(url,location):
        print("File ",str(i),"Downloaded")
    else:
        print("Not Able to download Fle")

def checkUTLink(url):
    if "youtube" in list(url.split(".")):
        return True
    return False

def multiFileDownload(localName,directory,playListsupport):
    i=1
    url=""
    try:
        with open(localName,"r") as r:
            url=r.readline()
            while url:
                print(url)
                url=''.join(url.split())
                if checkUTLink(url):
                    youtubeDownload.main(url,directory,playListsupport)   
                else:
                    downloader(url,directory,i)
                i+=1
                url=r.readline()
        
    except Exception as ex:
        print(ex)

    