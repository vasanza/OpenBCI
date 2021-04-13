import cv2
from pylsl import StreamInlet, resolve_stream
import pandas as pd
import random

DatosBEO, DatosLCH, DatosRCH, DatosLDF, DatosLPF, DatosRDF, DatosRPF = [], [], [], [], [], [], []
BEO, LCH, RCH, LDF, LPF, RDF, RPF = "1", "2", "3", "4", "5", "6", "7"
beo, lch, rch, ldf, lpf, rdf, rpf = 0, 0, 0, 0, 0, 0, 0


def mainlch():
    name = "S"+Subject+"R"+str(Run)+Tipo+LCH
    im = cv2.imread('D:/FIEC/F_BLOG/GITHUB/OpenBCI/Imagenes/LCH.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosLCH.append(sample)
        if len(DatosLCH) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosLCH)
            df.to_csv("D:/FIEC/F_BLOG/GITHUB/OpenBCI/Recoleccion/" + name + "_" +
                      str(lch) + '.csv')
            DatosLCH.clear()
            break


def mainrch():
    name = "S"+Subject+"R"+str(Run)+Tipo+RCH
    im = cv2.imread('D:/FIEC/F_BLOG/GITHUB/OpenBCI/Imagenes/RCH.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosRCH.append(sample)
        if len(DatosRCH) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosRCH)
            df.to_csv("D:/FIEC/F_BLOG/GITHUB/OpenBCI/Recoleccion/" + name+"_" +
                      str(rch) + '.csv')
            DatosRCH.clear()
            break


def mainldf():
    name = "S"+Subject+"R"+str(Run)+Tipo+LDF
    im = cv2.imread('D:/FIEC/F_BLOG/GITHUB/OpenBCI/Imagenes/LDF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosLDF.append(sample)
        if len(DatosLDF) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosLDF)
            df.to_csv("D:/FIEC/F_BLOG/GITHUB/OpenBCI/Recoleccion/" + name+"_" +
                      str(ldf) + '.csv')
            DatosLDF.clear()
            break


def mainlpf():
    name = "S"+Subject+"R"+str(Run)+Tipo+LPF
    im = cv2.imread('D:/FIEC/F_BLOG/GITHUB/OpenBCI/Imagenes/LPF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosLPF.append(sample)
        if len(DatosLPF) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosLPF)
            df.to_csv("D:/FIEC/F_BLOG/GITHUB/OpenBCI/Recoleccion/" + name + "_" +
                      str(lpf) + '.csv')
            DatosLPF.clear()
            break


def mainrdf():
    name = "S"+Subject+"R"+str(Run)+Tipo+RDF
    im = cv2.imread('D:/FIEC/F_BLOG/GITHUB/OpenBCI/Imagenes/RDF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosRDF.append(sample)
        if len(DatosRDF) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosRDF)
            df.to_csv("D:/FIEC/F_BLOG/GITHUB/OpenBCI/Recoleccion/" + name + "_" +
                      str(rdf) + '.csv')
            DatosRDF.clear()
            break


def mainrpf():
    name = "S"+Subject+"R"+str(Run)+Tipo+RPF
    im = cv2.imread('D:/FIEC/F_BLOG/GITHUB/OpenBCI/Imagenes/RPF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosRPF.append(sample)
        if len(DatosRPF) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosRPF)
            df.to_csv("D:/FIEC/F_BLOG/GITHUB/OpenBCI/Recoleccion/" + name + "_" +
                      str(rpf) + '.csv')
            DatosRPF.clear()
            break


def mainbeo():
    name = "S"+Subject+"R"+str(Run)+Tipo+BEO
    im = cv2.imread('D:/FIEC/F_BLOG/GITHUB/OpenBCI/Imagenes/Baseline.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosBEO.append(sample)
        if len(DatosBEO) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosBEO)
            df.to_csv("D:/FIEC/F_BLOG/GITHUB/OpenBCI/Recoleccion/" + name + "_" +
                      str(beo) + '.csv')
            DatosBEO.clear()
            break


def descanso():
    img = cv2.imread('D:/FIEC/F_BLOG/GITHUB/OpenBCI/Imagenes/Descanso.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Image', img)
    cv2.waitKey(4000)


operaciones = {'1': mainlch, '2': mainrch, '3': mainldf, '4': mainlpf, '5': mainrdf, '6': mainrpf}

Subject = input('Ingresar identificación del sujeto: ')
Tipo = input('Ingresar el tipo de experimento a realizar (M/I/O): ')   # Tipos posibles M , I , O
Run = int(input('Ingresar el número de serie: '))

print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
# inlet = StreamInlet(streams[0])

valores = 0

while __name__ == '__main__':
    descanso()
    mainbeo()
    beo += 1
    while valores != 30:
        valores = lch + rch + ldf + lpf + rdf + rpf
        print(valores)
        opcion = str(random.randint(1, 6))
        if opcion == '1' and lch != 5:
            operaciones[opcion]()
            descanso()
            lch += 1
        elif opcion == '2' and rch != 5:
            operaciones[opcion]()
            descanso()
            rch += 1
        elif opcion == '3' and ldf != 5:
            operaciones[opcion]()
            descanso()
            ldf += 1
        elif opcion == '4' and lpf != 5:
            operaciones[opcion]()
            descanso()
            lpf += 1
        elif opcion == '5' and rdf != 5:
            operaciones[opcion]()
            descanso()
            rdf += 1
        elif opcion == '6' and rpf != 5:
            operaciones[opcion]()
            descanso()
            rpf += 1
    valores, lch, rch, ldf, lpf, rdf, rpf = 0, 0, 0, 0, 0, 0, 0
    continuar = input("Desea continuar (S/N) :")
    if continuar == 'N':
        break
    else:
        Run += 1
