import cv2
import numpy as np
import sys

if(len(sys.argv) > 1):
    filename = sys.argv[1]
else:
    print('Pasaje de parametros incorrecto.')
    sys.exit()


drawing = False
Pts_i = np.empty([4, 2])
Pts_f = np.empty([4, 2])

P_i,P_f = (-1,-1),(-1,-1)

print(Pts_i)
# print(Pts[0,0])
# print(Pts[1,1])


count_pts = 0
PTS = 4
BLUE = (255,0,0)
GREEN = (0,255,0)
RED = (0,0,255)

def draw(event,current_X,current_Y,flags,param): #Dibuja en una cierta posicion de la pantalla
    global img,img2,count_pts,Pts

    if event == cv2.EVENT_LBUTTONDOWN :
        if count_pts == PTS:
            print(Pts_i)
            print("Reinicio de Puntos.")

        if count_pts < PTS :
            Pts_x , Pts_y = current_X, current_Y
            cv2.circle(img2,(Pts_x,Pts_y),5,GREEN,-1)
            Pts_i[count_pts,0],Pts_i[count_pts,1] = Pts_x,Pts_y
            print(f"Cor_X = {Pts_i[count_pts,0]} Cor_Y = {Pts_i[count_pts,1]}")
            count_pts += 1 

        else:
            img2 = img.copy()
            count_pts = 0


def rectificar(img2):
    global Pts_i,Pts_f,Mask_Higth,Mask_Width
    X = np.empty(4)
    Y = np.empty(4)
    for i in range(0,4):
        X[i] = Pts_i[i,0]
        Y[i] = Pts_i[i,1]

    Pts_i = np.float32([[X[0],Y[0]],[X[1],Y[1]],[X[2],Y[2]],[X[3],Y[3]]])
    Pts_f = np.float32([[int(Mask_Width/2-337*Resolution),int(Mask_Higth/2-337)],[int(Mask_Width/2+337*Resolution),int(Mask_Higth/2-337)], [int(Mask_Width/2-337*Resolution),int(Mask_Higth/2+337)],[int(Mask_Width/2+337*Resolution),int(Mask_Higth/2+337)]])

    M = cv2.getPerspectiveTransform(Pts_i,Pts_f)
    img3 = cv2.warpPerspective(img2,M,(Mask_Width,Mask_Higth))

    img4 = img3.copy()
    # cv2.imshow("Imagen2",img2)
    # cv2.imshow("Imagen3",img3)
    # cv2.imshow("Imagen4",img4)

def measure(event, x, y, flags, param):
    print("Measure")
    global P_i,P_f,img3,img4,drawing,Mask_Higth,Mask_Width

    if event == cv2.EVENT_LBUTTONDOWN:
        if P_i == (-1,-1):
            drawing = True
            P_i = (x, y)
        elif P_f == (-1,-1):
            drawing = False
            P_f = (x, y)
            cv2.circle(img3, P_f, 3, (0, 255, 0), -1)
        else:
            P_i, P_f = (-1,-1), (-1,-1)
            # img4=img3.copy()
    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img4 = img3.copy()
            cv2.circle(img4, P_i, 3, (0, 255, 0), -1)
            cv2.line(img4, P_i, (x, y), (0, 255, 0), 2)         
            X = int(np.sqrt(pow(P_i[0]-x,2)+pow(P_i[1]-y,2)))
            X = round(X*1000/674,3)
            cv2.putText(img4,str(X),(int(Mask_Width/2-40),25),cv2.FONT_HERSHEY_TRIPLEX,1,(150, 150, 100), 1, cv2.LINE_AA)
            print(X)
            print(f"Coordenadas iniciales : P_i[{P_i}]")

Patron = False
while not Patron:
    try:
        Pattern_Higth = int(input("Ingrese la altura Patron: "))
        Pattern_Width = int(input("Ingrese el ancho Patron: "))
        Resolution = Pattern_Higth/Pattern_Width
        print(f"La resolucion es {Resolution}")
        Patron = True

    except Exception as e:
        print(f"Ingresar los valores nuevamente no seai infeli.")


img = cv2.imread(filename)
img2 = img.copy()
WIDTHER ,HIGTHER, AXI = img.shape
cv2.namedWindow('imagen')
cv2.setMouseCallback('imagen',draw) 
cv2.namedWindow('Imagen Rectificada')
cv2.setMouseCallback('Imagen Rectificada',measure)
Mask_Higth,Mask_Width = 720, 1280

img3 = np.ones([Mask_Higth, Mask_Width])
img4 = img3.copy()

while 1:
    cv2.imshow("imagen",img2)
    cv2.imshow('Imagen Rectificada',img3)
    """print("Main")"""
    k = cv2.waitKey(1) & 0xFF

    if k == ord('d'):
        img2 = img.copy()
        rectificar(img2)

    elif k == ord ('r'):
        P_i,P_f = (-1,-1),(-1,-1)
        img2 = img.copy()

    elif k == ord('q'):
        sys.exit()
        break

cv2.destroyAllWindows()