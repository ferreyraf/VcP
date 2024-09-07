"""! /usr/bin/env python
*- coding: utf-8 -*-
"""
"""
    Este programa utiliza la libreria de OpenCV para procesar
    una imagen en escala de grises y luego la segmenta en blanco
    y negro solo para distinguir formas.
"""
import cv2
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print(f"Parametro incorrectos")
    sys.exit()

# Abre una imagen con OpenCV.
# Una imagen se separa en 3 capas de colores, RGB.
# cv2 tiene la particularidad de trabajar con BGR.
# Tiene opciones para cambiar de sistemas de colores
# BGR2RGB
# Abre la imagen en escala de grises
img = cv2.imread('hoja.png',0 )

# Muestra la imagen con un titulo.
cv2.imshow("Imagen en escala de Girses.",img)
# Espera a que el usuario toque una letra para continuar el codigo.
cv2.waitKey(0)

x=len(img)
for ROW in range (0,x):
    for COL in range (0,x):
        if(img[ROW,COL]>50):
            img[ROW,COL]=255
        else:
            img[ROW,COL]=0
            
cv2.imshow("Imagen Segmentada",img)

cv2.waitKey(0)
sys.exit()
cv2.destroyAllWindows()