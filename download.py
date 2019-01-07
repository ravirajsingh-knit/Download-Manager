import requests
import sys
import mimetypes
import os
import threading

def split_poss(length):
    indexList=[]
    if length/8>4096:
        print("Required Split")
        start=length/8
        for i in range(8):
            indexList.append(int(i*start))
        indexList.append(length)
    else:
        print("No Split Require")
        indexList.append(0)
    return indexList

def checkForSupport(url):
    headers = {"Range": "bytes=0-0"}
    response=requests.head(url,headers=headers,allow_redirects=True)
    print(response.status_code)
    if response.status_code==206:
        return True
    else:
        return False
    
def data_info(url):
    try:
        response= requests.head(url,allow_redirects=True)
        print(response.status_code)
        if response.status_code==200:
            contents=response.headers
            length=-1
            name=None
            extension=None
            if 'Content-Length' in contents.keys():
                length=int(contents['Content-Length'])
            if 'Content-Disposition' in contents.keys():
                name=contents['Content-Disposition']
            else:
                name=url[url.rfind("/")+1:]
            if 'Content-Type' in contents.keys():
                extension=mimetypes.guess_extension(contents['Content-Type'])
            return length,name
        else:
            print("Failed to connect")
    except Exception as ex:
        print(str(ex))
        sys.exit(-1)

def simple_download(url,name,location):
    data = requests.get(url, stream=True)
    with open(os.path.join(location,name),'wb') as wr:
        for chunk in data.iter_content(chunk_size=1024):
            if chunk: 
                wr.write(chunk)
    return True

def download(url,start,end,location,name,id):
    headers = {"Range": "bytes="+str(start)+"-"+str(end)}
    print(start," ",end)
    data=requests.get(url,headers=headers, stream=True,allow_redirects=True)
    #print("thread ",start," ",end," ",response.text)
    with open(os.path.join(location,name+"_"+str(id)),'wb') as wr:
        for chunk in data.iter_content(chunk_size=1024):
            if chunk: 
                wr.write(chunk)


def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data
    

def mergefile(location,name):
    with open(os.path.join(location,name),'wb') as wr:
        for i in range(8):
            with open(os.path.join(location,name+"_"+str(i)),'rb') as rb:
                for data in read_in_chunks(rb):
                    wr.write(data)


def deleteTemp(location,name):
    for i in range(8):
        os.remove(os.path.join(location,name+"_"+str(i)))

def multithreadDownload(url,name,location,indexList):
    numberThread=len(indexList)-1
    threadList=[]
    for i in range(numberThread):
        start=indexList[i]
        end=indexList[i+1]-1
        thread = threading.Thread(target=download,args=(url,start,end,location,name,i))
        thread.start()
        threadList.append(thread)
    
    for thread in threadList:
        thread.join()
    mergefile(location,name)
    deleteTemp(location,name)
    return True


def download_file(url,location):
    try:
        length,name=data_info(url)
        print(length,name)    
        if length==-1 or (not checkForSupport(url)):
            print("Going for one thread Download")
            simple_download(url,name,location)
        else:
            print("Going for multithread download")
            indexList=split_poss(length)
            multithreadDownload(url,name,location,indexList)
    except Exception as ex:
        print(ex)
        return False
    
    return True


