import cv2
import dropbox
import time
import random
start=time.time()
def takePic():
    number=random.randint(0,100)
    capture=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=capture.read()
        img="img"+str(number)+".png"
        cv2.imwrite(img,frame)
        start=time.time()
        result=False
        return img
    capture.release()
    cv2.destroyAllWindows()
def uploadFile(img):
    access_token='mdQ6MFffuLUAAAAAAAAAAe9uvjY0JIVg7IObWczfd_qMxk_wNlejn7WwNk-W3OE3'
    file=img
    file_from=file
    file_to="/test/"+(img)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
def main():
    while(True):
        if((time.time()-start)>=5):
            name=takePic()
            uploadFile(name)
main()                        