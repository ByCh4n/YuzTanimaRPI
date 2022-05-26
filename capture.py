import cv2
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()

    cv2.imshow("1",frame)
    if cv2.waitKey(10) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()    