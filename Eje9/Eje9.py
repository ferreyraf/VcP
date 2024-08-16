import cv2
import numpy as np
import sys

drawing = False # true if mouse is pressed
P_i,P_f = (-1,-1),(-1,-1)
"Pasaje de imagen como Argumento"

if(len(sys.argv) > 1):
    filename = sys.argv[1]
else:
    print('Pasaje de parametros incorrecto.')

print(sys.argv)


pt1,pt2,pt3,pt4 = (338,230), (985,245), (212,507), (1101,523)

"Eventos del mouse"

def draw(event,x,y,flags,param):
    global Pts1,drawing,img2,contador,img
    
    cv2.circle(img2,pt1,5,(0,255,0),-1)
    cv2.circle(img2,pt2,5,(0,255,0),-1)
    cv2.circle(img2,pt3,5,(0,255,0),-1)
    cv2.circle(img2,pt4,5,(0,255,0),-1)

def funcion_Rectificar(img2):
    global img3,img4,img,w,h
    img2=img.copy()
    Pts1 = np.float32([[338,230],[983,245],[212,507],[1101,523]])
    Pts2 = np.float32([[int(w/2-337*1344/1000),int(h/2-337)],[int(w/2+337*1344/1000),int(h/2-337)], [int(w/2-337*1344/1000),int(h/2+337)],[int(w/2+337*1344/1000),int(h/2+337)]])
    M = cv2.getPerspectiveTransform(Pts1,Pts2)
    img3 = cv2.warpPerspective(img2,M,(w,h))
    img4=img3.copy()


def measure(event, x, y, flags, param):
    global P_i,P_f,img3,img4,drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        if P_i == (-1,-1):
            drawing = True
            P_i = (x, y)
        elif P_f == (-1,-1):
            drawing = False
            P_f = (x, y)
            cv2.circle(img4, P_f, 3, (0, 255, 0), -1)
        else:
            P_i, P_f = (-1,-1), (-1,-1)
            img4=img3.copy()
    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img4 = img3.copy()
            cv2.circle(img4, P_i, 3, (0, 255, 0), -1)
            cv2.line(img4, P_i, (x, y), (0, 255, 0), 2)         
            X = int(np.sqrt(pow(P_i[0]-x,2)+pow(P_i[1]-y,2)))
            X = round(X*1000/674,3)
            cv2.putText(img4,str(X),(int(w/2-40),25),cv2.FONT_HERSHEY_TRIPLEX,1,(0, 255, 0), 1, cv2.LINE_AA)


img = cv2.imread(filename)
img2 = img.copy()
cv2.namedWindow('imagen')
cv2.setMouseCallback('imagen',draw)
cv2.namedWindow('Imagen Rectificada')
cv2.setMouseCallback('Imagen Rectificada',measure)
h,w = 720, 1280
img3 = np.zeros([h, w])
img4 = img3.copy()

while(1):
    cv2.imshow('imagen',img2)
    cv2.imshow('Imagen Rectificada',img4)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('h'):
        img2 = img.copy()
        funcion_Rectificar(img2)
    elif k == ord ('r'):
        P_i,P_f = (-1,-1),(-1,-1)
        img2 = img.copy()
    elif k == ord('q'):
        break
cv2.destroyAllWindows()
