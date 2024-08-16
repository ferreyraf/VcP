import cv2
import numpy as np

# Abre una imagen con todos los colores
img = cv2.imread('hoja.png', 1) # Rango de colores = 1 ,Escala de grises = 0
highter,widther,axi = img.shape

img_Blue = np.zeros((highter,widther,3),dtype=np.uint8) 
img_Blue[:,:,0] = img[:,:,0] 

img_Green = np.zeros((highter,widther,3),dtype=np.uint8) 
img_Green[:,:,1] = img[:,:,1] 

img_Red = np.zeros((highter,widther,3),dtype=np.uint8) 
img_Red[:,:,2] = img[:,:,2] 

img_Blue_Red = np.zeros((highter,widther,3),dtype=np.uint8)
img_Blue_Red = img_Blue+img_Red
img_Blue_Green = np.zeros((highter,widther,3),dtype=np.uint8)
img_Blue_Green = img_Blue+img_Green
img_Red_Green = np.zeros((highter,widther,3),dtype=np.uint8)
img_Red_Green = img_Green+img_Red

# img_Blue_Red[:,:,:]


print(img_Blue)
print(img.ndim)

cv2.imshow("Channel Blue",img_Blue)
cv2.imshow("Channel Green",img_Green)
cv2.imshow("Channel Red",img_Red)

cv2.imshow("Channel Blue",img_Blue_Red)
cv2.imshow("Channel Green",img_Blue_Green)
cv2.imshow("Channel Red",img_Red_Green)


print(f"Tamaño de las matrices Channel_Blue[0]\n{img_Blue[:,:,0]}")
print(f"Tamaño de las matrices Channel_Blue[1]\n{img_Blue[:,:,1]}")
print(f"Tamaño de las matrices Channel_Blue[2]\n{img_Blue[:,:,2]}")

# print(f"Tamaño de las matrices Green\t{}")
# print(f"Tamaño de las matrices Red\t{}")

print(f"Alto : {highter} , Ancho : {widther} y tiene {axi} dimensiones.")

print(type(img)) #BGR

Channel_Red = np.zeros((highter,widther,3),dtype=np.uint8) 
copi = Channel_Red.copy()

h_R,w_R,axi = Channel_Red.shape
# print(f"Alto : {h_R} , Ancho : {w_R} y tiene {axis_R} dimensiones.")
# cv2.imshow("ZEROS",Channel_Red)

# for fil in range(highter):
#     for col in range(widther):
#         if fil%2 and col%2:
#             copi[fil,col] = 100

# cv2.imshow("Cosa",copi)


cv2.waitKey(0)
