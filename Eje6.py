import cv2
import sys
import numpy as np
import math


drawing = False # true if mouse is pressed
i_x , i_y = -1 ,-1
f_x, f_y = -1, -1


"Pasaje de imagen como Argumento"

if(len(sys.argv) > 1):
    filename = sys.argv[1]
else:
    print('Pasaje de parametros incorrecto.')
    sys.exit(0)

"Transformacion de pixel"
def Func_Euclidia(tras_X, tras_Y, rot, img2,i_x, f_x, i_y, f_y,S):
    img2[:] = 0
    M=np.array([[S*math.cos(rot),       S*math.sin(rot),    tras_X],
                [S*math.sin(-rot),      S*math.cos(rot),    tras_Y],
                [       0       ,       0       ,   1    ]])
                
    for fil in range (0, f_x-i_x):
        for col in range (0, f_y-i_y):
            A = np.array([[fil],[col],[1]])
            A = np.transpose(np.dot(M,A))
            A[0,0] = A[0,0]/A[0,2]
            A[0,1] = A[0,1]/A[0,2]
            img2[i_y+int(A[0,1]),i_x+int(A[0,0]),:] = img[i_y+col,i_x+fil,:]

"Eventos del mouse"

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

img=cv2.imread(filename)
img2=img.copy() 
cv2.namedWindow ('image')
cv2.setMouseCallback('image',draw_circle)


"Pasaje de datos"
tras_X=int(input("Traslacion en X: "))
tras_Y=int(input("Traslacion en Y: "))
rot = math.radians((int(input("Angulo de rotación: "))))
S=float(input("Factor de escala: "))


print(rot)
print(tras_X)
print(tras_Y)

while(1):
    cv2.imshow('image',img2)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('s'):
        if i_x>f_x:
            aux = i_x
            i_x = f_x
            f_x = aux
        if i_y>f_y:
            aux = i_y
            i_y = f_y
            f_y = aux
        img2=img.copy()
        Func_Euclidia(tras_X, tras_Y, rot, img2,i_x, f_x, i_y, f_y,S)
        cv2.imwrite('Imagenguardada.png', img2[:,:,:])
    elif k == ord ('r'):
        img2 = img.copy()
    elif k == ord('q'):
        break
cv2.destroyAllWindows()


