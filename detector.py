import cv2
import mediapipe as mp
import numpy as np
import math
import serial, time

arduino = serial.Serial("/dev/ttyACM0", 115200)

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For static images:
IMAGE_FILES = []

# Definicion de dedos.
THUMB = np.empty([4, 2])
INDEX = np.empty([4, 2])
MIDDLE = np.empty([4, 2])
RING = np.empty([4, 2])
PINKY = np.empty([4, 2])

# print(THUMB)
# print(INDEX)
# print(MIDDLE)
# print(RING)
# print(PINKY)


def Show_Coor(nombre,dedo,w,h):
  for i in range(0,4):
    print(f"{nombre} X[{dedo[i,0]*w}] \tY[{dedo[i,1]*h}]")

def dibujar_recta(image,Pi_x,Pi_y,Pf_x,Pf_y):
  Pi_x = int(Pi_x)
  Pi_y = int(Pi_x)
  Pf_x = int(Pf_x)
  Pf_y = int(Pf_y)

  cv2.line(image,(Pi_x,Pi_y),(Pf_x,Pf_y),(0,255,0),2)

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    image_height, image_width, _ = image.shape
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        # print('hand_landmarks:', hand_landmarks),

        # PULGAR
        THUMB[0,0] = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x
        THUMB[0,1] = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y
        THUMB[1,0] = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x
        THUMB[1,1] = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
        THUMB[2,0] = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x
        THUMB[2,1] = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y
        THUMB[3,0] = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
        THUMB[3,1] = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y

        # INDICE
        INDEX[0,0] = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x
        INDEX[0,1] = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
        INDEX[1,0] = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x
        INDEX[1,1] = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
        INDEX[2,0] = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x
        INDEX[2,1] = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y
        INDEX[3,0] = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
        INDEX[3,1] = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y

  
        # MAYOR
        MIDDLE[0,0] = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x
        MIDDLE[0,1] = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
        MIDDLE[1,0] = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x
        MIDDLE[1,1] = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
        MIDDLE[2,0] = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x
        MIDDLE[2,1] = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y
        MIDDLE[3,0] = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
        MIDDLE[3,1] = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
  

        # ANULAR
        RING[0,0] = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x
        RING[0,1] = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
        RING[1,0] = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x
        RING[1,1] = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
        RING[2,0] = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x
        RING[2,1] = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y
        RING[3,0] = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x
        RING[3,1] = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y


        # MEÑIQUE
        PINKY[0,0] = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x
        PINKY[0,1] = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y
        PINKY[1,0] = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x
        PINKY[1,1] = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y
        PINKY[2,0] = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x
        PINKY[2,1] = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y
        PINKY[3,0] = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x
        PINKY[3,1] = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

        Show_Coor("PULGAR",THUMB,image_width,image_height)
        print('\n')
        Show_Coor("INDICE",INDEX,image_width,image_height)
        print('\n')
        Show_Coor("MAYOR",MIDDLE,image_width,image_height)
        print('\n')
        Show_Coor("ANULAR",RING,image_width,image_height)
        print('\n')
        Show_Coor("MEÑIQUE",PINKY,image_width,image_height)
        print('\n')
        print(f'Tamaño de la imagen\n Alto :{image_height} \t Ancho :{image_width}')
        print(f'INDICE[8] : X[{INDEX[3,0]*image_width}]\t Y[{INDEX[3,1]*image_height}]')
        print(f'PULGAR[4] : X[{THUMB[3,0]*image_width}]\t Y[{THUMB[3,1]*image_height}]')

        Pi_x = int(INDEX[3,0]*image_width)
        Pi_y = int(INDEX[3,1]*image_height)
        Pf_x = int(THUMB[3,0]*image_width)
        Pf_y = int(THUMB[3,1]*image_height)

        cv2.line(image,(Pi_x,Pi_y),(Pf_x,Pf_y),(0,255,0),2)

        Xs = pow((Pi_x-Pf_x),2)
        Ys = pow((Pi_y-Pf_y),2)

        # print(Xs)
        recta = math.sqrt(Xs+Ys)
        print(f'Distancia en pixeles d : {recta}')

        Rojo = 100

        if recta < Rojo :
          # pass
          arduino.write(b'0')
          # arduino.close()
        elif recta > Rojo:
          # pass
          arduino.write(b'1')
          # arduino.close()1

        # cv2.line(image,(Pi_x,Pi_y),(Pf_x,Pf_y),(0,255,0),2)
        # dibujar_recta(image,THUMB[3,0],THUMB[3,1],INDEX[3,0],INDEX[3,1])

        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    cv2.line(image,(0,0),(100,100),(0,255,0),2)
    if cv2.waitKey(5) & 0xFF == 27:
      break

arduino.close()
cap.release()




# with mp_hands.Hands(
#     static_image_mode=True,
#     max_num_hands=2,
#     min_detection_confidence=0.5) as hands:
#   print(f"Inicio del modelo.")
#   for idx, file in enumerate(IMAGE_FILES):
#     # Read an image, flip it around y-axis for correct handedness output (see
#     # above).
#     print(f'Carga el frame del video.')
#     image = cv2.flip(cv2.imread(file), 1)
#     # Convert the BGR image to RGB before processing.
#     results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

#     # Print handedness and draw hand landmarks on the image.
#     print('Handedness:', results.multi_handedness)
#     if not results.multi_hand_landmarks:
#       continue
#     image_height, image_width, _ = image.shape
#     annotated_image = image.copy()

#     for hand_landmarks in results.multi_hand_landmarks:
#       print('hand_landmarks:', hand_landmarks)
#       print(
#           f'Index finger tip coordinates: (',
#           f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
#           f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
#       )
#       mp_drawing.draw_landmarks(
#           annotated_image,
#           hand_landmarks,
#           mp_hands.HAND_CONNECTIONS, 
#           mp_drawing_styles.get_default_hand_landmarks_style(),
#           mp_drawing_styles.get_default_hand_connections_style())
#     cv2.imwrite(
#         '/tmp/annotated_image' + str(idx) + '.png', cv2.flip(annotated_image, 1))
#     # Draw hand world landmarks.
#     if not results.multi_hand_world_landmarks:
#       continue
#     for hand_world_landmarks in results.multi_hand_world_landmarks:
#       mp_drawing.plot_landmarks(
#         hand_world_landmarks, mp_hands.HAND_CONNECTIONS, azimuth=5)
