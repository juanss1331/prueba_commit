import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2

"""
Esta e la forma de realizar un comentario en bloque en python.
Este codigo requiere tener instaladas varias librerias
para esto requieren abir la consola de comandos y escribir

conda install opencv=3.4.2
con este comando le estamos diciendo al anaconda que porfavor nos descargue el paquete
opencv en la version 3.4.2

es codigo pone un recuadro sobre nuestra cara usando la camara del portatil :D
"""

print("Este codigo es simplemente un ejemplo para hacerle push a la nube.")

cascada_cara = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detectar_cara(imagen):
    imagen1 = imagen.copy()
    rectangulos = cascada_cara.detectMultiScale(imagen1)
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen1,(x,y),(x+w,y+h),(255,0,0),10)
    return(imagen1)

captura = cv2.VideoCapture(0)

while True:
    resultado,video = captura.read()
    video = detectar_cara(video)
    cv2.imshow('Nuestro videocon rectangulo',video)

    if cv2.waitKey(10) & 0xFF ==ord('q'):
        break

captura.release()
cv2.destroyAllWindows()

