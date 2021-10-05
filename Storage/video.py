import cv2
def take_snapshort():
    videocaptuerobject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocaptuerobject.read()
        cv2.imwrite("picture.jpg",frame)
        result=False
    videocaptuerobject.release()
    cv2.destroyAllWindows()
take_snapshort()