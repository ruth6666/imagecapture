import cv2
import dropbox
import time
import random

startTime = time.time()
def takeSnapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        imgName = 'img'+str(number)+'.png'      
        cv2.imwrite(imgName,frame)
        startTime = time.time()
        result = False
    return imgName
    print('Snapshot taken.')
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(imgName):
    accessToken = 'RjubiHx6ExIAAAAAAAAAASsf7YKLBDcgZHFhWCmdBztYekeUUjdYyM8Z5W4MGN9e'
    file = imgName
    fileFrom = file
    fileTo = '/testfolder/'+(imgName)
    dbx = dropbox.Dropbox(accessToken)
    with open(fileFrom,'rb') as f:
        dbx.files_upload(f.read(),fileTo,mode=dropbox.files.WriteMode.overwrite)
        print('File uploaded.')

def main():
    while(True):
        if((time.time()-startTime)>=5):
            name = takeSnapshot()
            uploadFile(name)
main()