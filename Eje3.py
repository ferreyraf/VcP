#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import cv2

# if len(sys.argv) > 1 :
#     filename = sys.argv[1]
# else:
#     print('Pass a file name as first argument')
#     sys.exit(0)

cap = cv2.VideoCapture(0)
high = int(cap.get(4))
width = int(cap.get(3))
fps = int(cap.get(5))

fourcc = cv2.VideoWriter_fourcc('X' ,'V' ,'I' ,'D')
framesize = (width, high)

out = cv2.VideoWriter('output.avi', fourcc , fps , framesize, 0)

delay = int(1000/fps)


while (cap.isOpened()):

    ret,frame = cap.read()
    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(gray)
        cv2.imshow('Image gray', gray)
        
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    else:
        break
        
cap.release()
out.release()
cv2.destroyAllWindows()