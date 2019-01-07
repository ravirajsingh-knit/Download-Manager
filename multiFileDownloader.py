import main
import queue
import threading
def downloader(url,location,i):
    print("Starting Download File ",str(i))
    if main.main(url,location):
        print("File ",str(i),"Downloaded")
    else:
        print("Not Able to download Fle")

def multiFileDownload():
    localName=input("File Name ")
    directory=input("Directory ")
    i=1
    url=""
    try:
        with open(localName,"r") as r:
            url=r.readline()
            while url:
                print(url)
                url=''.join(url.split())
                downloader(url,directory,i)
                i+=1
                url=r.readline()
        
    except Exception as ex:
        print(ex)

if __name__=="__main__":
    multiFileDownload()
    