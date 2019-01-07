import download
#from Download_Manager.download import download_file
def main(url,location):
    if download.download_file(url,location):
        print("File is downloaded as")
        return True
    else:
        print("Some problem occurs")
        return False

def withOutGui():
    url=input("URL")
    location=input("Location")
    main(url,location)



if __name__=="__main__":
    withOutGui()
    