import cv2
import sys
drawing = False # true if mouse is pressed
i_x , i_y = -1 ,-1
f_x, f_y = -1, -1

def draw_circle(event,x,y,flags,param):
    global i_x,i_y,drawing ,f_x ,f_y,img2,img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        i_x , i_y = x , y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            img2 = img.copy()
            cv2.rectangle(img2,(i_x,i_y),(x,y),(0,0,255),2)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        img2 = img.copy()
        cv2.rectangle(img2,(i_x,i_y),(x,y),(0,0,0),2)
        f_x , f_y = x , y
if(len(sys.argv) > 1):
    filename = sys.argv[1]
else:
    print('Parametro incorrecto.')
    sys.exit(0)

img = cv2.imread(filename)
cv2.namedWindow ('image')
cv2.setMouseCallback('image',draw_circle)
img2 = img.copy()

while(1):
    cv2.imshow('image',img2)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('g'):
        if i_x>f_x:
            aux = i_x
            i_x = f_x
            f_x = aux
        if i_y>f_y:
            aux = i_y
            i_y = f_y
            f_y = aux
        cv2.imwrite('Imagen Guardada.png',img[i_y:f_y,i_x:f_x,:])
    elif k == ord ('r'):
        img2 = img.copy()
    elif k == ord('q'):
        break
cv2.destroyAllWindows()

