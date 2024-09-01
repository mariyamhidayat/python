from pyzbar.pyzbar import decode
import cv2
import pyzbar.pyzbar as pyzbar
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    
    decode_qr=pyzbar.decode(frame)
    for qrcode in decode_qr:
        (x,y,w,h)=qrcode.rect
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("qr code scanner ",frame)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()