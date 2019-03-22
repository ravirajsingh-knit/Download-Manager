from shutil import copyfile
import download
import multiFileDownloader
import youtubeDownload
import json
import os
def main():
    try:
        if not os.path.exists("conf.json"):
            copyfile(".conf","conf.json")
        conf=None
        with open('conf.json') as f:
            conf = json.load(f)
        multiFileDownloader.multiFileDownload(conf["inputFileLoc"],conf["outputFolder"],conf["playListsupport"])
    except Exception as exp:
        print(getattr(exp, 'message', str(exp)))

if __name__=="__main__":
    main()



