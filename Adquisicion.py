import cv2
from pylsl import StreamInlet, resolve_stream
import pandas as pd
import random

DatosSiz, DatosIiz, DatosSde, DatosIde = [], [], [], []
Siz, Iiz, Sde, Ide = "1", "2", "3", "4"
siz, iiz, sde, ide = 0, 0, 0, 0


def mainsiz():
    name = "S"+Subject+"R"+str(Run)+Tipo+Siz
    im = cv2.imread('D:/FIEC/F_BLOG/GITHUB/OpenBCI/Imagenes/Siz.jpg')  # Cambiar el nombre correspondiente
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosSiz.append(sample)
        if len(DatosSiz) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosSiz)
            df.to_csv("D:/FIEC/F_BLOG/GITHUB/OpenBCI/DatosRecolectados/" + name + "_" +
                      str(siz) + '.csv')
            DatosSiz.clear()
            break


def mainiiz():
    name = "S"+Subject+"R"+str(Run)+Tipo+Iiz
    im = cv2.imread('D:/FIEC/F_BLOG/GITHUB/OpenBCI/Imagenes/RCH.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosIiz.append(sample)
        if len(DatosIiz) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosIiz)
            df.to_csv("D:/FIEC/F_BLOG/GITHUB/OpenBCI/DatosRecolectados/" + name+"_" +
                      str(iiz) + '.csv')
            DatosIiz.clear()
            break


def mainsde():
    name = "S"+Subject+"R"+str(Run)+Tipo+Sde
    im = cv2.imread('D:/FIEC/F_BLOG/GITHUB/OpenBCI/Imagenes/LDF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosSde.append(sample)
        if len(DatosSde) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosSde)
            df.to_csv("D:/FIEC/F_BLOG/GITHUB/OpenBCI/DatosRecolectados/" + name+"_" +
                      str(sde) + '.csv')
            DatosSde.clear()
            break


def mainide():
    name = "S"+Subject+"R"+str(Run)+Tipo+Ide
    im = cv2.imread('D:/FIEC/F_BLOG/GITHUB/OpenBCI/Imagenes/LPF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosIde.append(sample)
        if len(DatosIde) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosIde)
            df.to_csv("D:/FIEC/F_BLOG/GITHUB/OpenBCI/DatosRecolectados/" + name + "_" +
                      str(ide) + '.csv')
            DatosIde.clear()
            break


def descanso():
    img = cv2.imread('D:/FIEC/F_BLOG/GITHUB/OpenBCI/Imagenes/Descanso.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Image', img)
    cv2.waitKey(4000)


operaciones = {'1': mainsiz, '2': mainiiz, '3': mainsde, '4': mainiiz}

Subject = input('Ingresar identificación del sujeto: ')
Tipo = input('Ingresar el tipo de experimento a realizar (M/I/O): ')   # Tipos posibles M , I , O
Run = int(input('Ingresar el número de serie: '))

print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
# inlet = StreamInlet(streams[0])

valores = 0

while __name__ == '__main__':
    descanso()
    while valores != 20:
        valores = siz + iiz + sde + siz
        print(valores)
        opcion = str(random.randint(1, 6))
        if opcion == '1' and siz != 5:
            operaciones[opcion]()
            descanso()
            siz += 1
        elif opcion == '2' and iiz != 5:
            operaciones[opcion]()
            descanso()
            iiz += 1
        elif opcion == '3' and sde != 5:
            operaciones[opcion]()
            descanso()
            sde += 1
        elif opcion == '4' and ide != 5:
            operaciones[opcion]()
            descanso()
            ide += 1
    valores, siz, iiz, sde, ide = 0, 0, 0, 0, 0
    continuar = input("Desea continuar (S/N) :")
    if continuar == 'N':
        break
    else:
        Run += 1
