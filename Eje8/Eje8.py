import cv2
import numpy as np
import sys

drawing = False # true if mouse is pressed

"Pasaje de imagen como Argumento"

if(len(sys.argv) > 1):
    filename = sys.argv[1]
else:
    print('Pasaje de parametros incorrecto.')

print(sys.argv)

Pts1 = np.float32([[0,0],[0,0],[0,0],[0,0]])
contador = 0
"Eventos del mouse"

def draw(event,x,y,flags,param):
    global Pts1,drawing,img2,contador,img
    if event == cv2.EVENT_LBUTTONDOWN :
        if(contador<4):
            drawing = True
            Pi = x, y
            cv2.circle(img2,Pi,5,(0,255,0),-1)
            Pts1[contador,0],Pts1[contador,1] = Pi
            contador+=1 
        else:
            draw= False
            img2=img.copy()
            contador = 0
            Pts1=np.float32([[-1,-1],
                            [-1,-1],
                            [-1,-1],
                            [-1,-1]])


def funcion_Rectificar(img2,Pts1):
    Pts2 = np.float32([[0,0],[719,0],[0,719],[719,719]])
    M = cv2.getPerspectiveTransform(Pts1,Pts2)
    img2 = cv2.warpPerspective(img2,M,(719,719))
    cv2.imshow("Transformacion",img2)
    cv2.imwrite("salida.png",img2)



img = cv2.imread(filename)
img2 = img.copy()
cv2.namedWindow('imagen')
cv2.setMouseCallback('imagen',draw)




while(1):
    cv2.imshow('imagen',img2)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('h'):
        img2 = img.copy()
        funcion_Rectificar(img2,Pts1)
    elif k == ord ('r'):
        contador=0
        img2 = img.copy()
    elif k == ord('q'):
        break
cv2.destroyAllWindows()
