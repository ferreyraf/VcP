import cv2
import sys
import numpy as np
import math

drawing = False # true if mouse is pressed

"Pasaje de imagen como Argumento"

if(len(sys.argv) > 1):
    filename_1 = sys.argv[1]
    filename_2 = sys.argv[2] 
else:
    print('Pasaje de parametros incorrecto.')

print(sys.argv)

contador = 0
Pts1 =np.float32([[0,0],
        [0,0],
        [0,0]])
"Eventos del mouse"

def draw(event,x,y,flags,param):
    global Pts1,drawing,img2,contador,img
    if event == cv2.EVENT_LBUTTONDOWN :
        if(contador<3):
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
                            [-1,-1]])

def funcion_Affine(img2,logo,Pts1):
    global h_1,h_2,w_1,w_2
    Pts2 =np.float32([[0,0],[w_1,0],[0,h_1]])
    M = cv2.getAffineTransform(Pts2,Pts1)
    logo=cv2.warpAffine(logo,M,(w_2,h_2))
    ind = np.sum(logo,axis=2) != 0
    img2[ind] =logo[ind] 
    cv2.imshow('Funcion con Transformacion Affine',img2)
    cv2.imwrite('Salida.png',img2)
    

img=cv2.imread(filename_1)
logo=cv2.imread(filename_2)
img2=img.copy() 
h_2=img.shape[0]
w_2=img.shape[1]
h_1=logo.shape[0]
w_1=logo.shape[1]

print(h_1)
print(w_1)

print(h_2)
print(w_2)

img2=img.copy() 
cv2.namedWindow ('image')
cv2.setMouseCallback('image',draw)

while(1):
    cv2.imshow('image',img2)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('a'):
        funcion_Affine(img2,logo,Pts1)
    elif k == ord ('r'):
        contador=0
        img2 = img.copy()
    elif k == ord('q'):
        break
cv2.destroyAllWindows()

